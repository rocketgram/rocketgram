# Copyright (C) 2015-2019 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


import asyncio
import json
import logging

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
                data = aiohttp.FormData()
                for name, field in request_data.items():
                    if isinstance(field, (dict, list)):
                        data.add_field(name, json_encoder(field), content_type='application/json')
                        continue
                    data.add_field(name, str(field), content_type='text/plain')

                for file in files:
                    data.add_field(file.file_name, file.data, filename=file.file_name, content_type=file.content_type)

                response = await self._session.post(url, data=data, timeout=self._timeout)
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
