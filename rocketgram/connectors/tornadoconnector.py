# Copyright (C) 2015-2019 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


import asyncio
import json
import logging
import uuid

from tornado.httpclient import AsyncHTTPClient, HTTPRequest

from .connector import Connector, USER_AGENT
from .. import types
from ..errors import RocketgramNetworkError, RocketgramParseError
from ..requests import Request
from ..update import Response

json_encoder = json.dumps
json_decoder = json.loads

try:
    import ujson

    json_encoder = ujson.dumps
    json_decoder = ujson.loads
except ModuleNotFoundError:
    pass

logger = logging.getLogger('rocketgram.connectors.tornadoconnector')

HEADERS = {'Content-Type': 'application/json', 'User-Agent': USER_AGENT}


class TornadoConnector(Connector):
    __slots__ = ('_api_url', '_client', '_timeout')

    def __init__(self, *, timeout: int = 35, api_url: str = types.API_URL):
        self._api_url = api_url
        self._client = AsyncHTTPClient()
        self._timeout = timeout

    async def init(self):
        pass

    async def shutdown(self):
        pass

    async def send(self, token: str, request: Request) -> Response:
        try:
            url = self._api_url % token + request.method

            request_data = request.render()

            files = request.files()

            if len(files):
                boundary = uuid.uuid4().hex

                async def producer(write):
                    for name, field in request_data.items():
                        if isinstance(field, (dict, list)):
                            content_type = 'application/json'
                            data = json_encoder(field)
                        else:
                            content_type = 'text/plain'
                            data = str(field)

                        buf = f'--{boundary}\r\n' \
                            f'Content-Disposition: form-data; name="{name}"\r\n' \
                            f'Content-Type: {content_type}\r\n\r\n' \
                            f'{data}' \
                            f'\r\n'

                        await write(buf.encode())
                        continue

                    for fl in files:
                        begin = f'--{boundary}\r\n' \
                            f'Content-Disposition: form-data; name="{fl.file_name}"; filename="{fl.file_name}"\r\n' \
                            f'Content-Type: {fl.content_type}\r\n' \
                            f'\r\n'

                        await write(begin.encode())

                        while True:
                            chunk = fl.data.read(8 * 1024)
                            if not chunk:
                                break
                            await write(chunk)

                        await write(f'\r\n'.encode())

                    await write(f'--{boundary}--\r\n\r\n'.encode())

                headers = {
                    'Content-Type': f'multipart/form-data; boundary={boundary}',
                    'User-Agent': USER_AGENT
                }

                req = HTTPRequest(url, method='POST', headers=headers, body_producer=producer,
                                  request_timeout=self._timeout)
            else:
                req = HTTPRequest(url, method='POST', headers=HEADERS, body=json_encoder(request_data),
                                  request_timeout=self._timeout)

            response = await self._client.fetch(req, raise_error=False)

            return Response.parse(json_decoder(response.body), request)
        except json.decoder.JSONDecodeError as e:
            raise RocketgramParseError(e)
        except asyncio.CancelledError:
            raise
        except Exception as e:
            raise RocketgramNetworkError(e)
