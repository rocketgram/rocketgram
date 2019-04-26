# Copyright (C) 2015-2019 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


import asyncio
import json
import logging

import aiohttp

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

logger = logging.getLogger('rocketgram.connectors.aiohttpconnector')

HEADERS = {'Content-Type': 'application/json', 'User-Agent': USER_AGENT}


class AioHttpConnector(Connector):
    __slots__ = ('_api_url', '_session', '_timeout')

    def __init__(self, *, timeout: int = 35, api_url: str = types.API_URL):
        self._api_url = api_url
        self._session = aiohttp.ClientSession(loop=asyncio.get_event_loop())
        self._timeout = timeout

    async def init(self):
        pass

    async def shutdown(self):
        await self._session.close()

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
                response = await self._session.post(url, data=json_encoder(request_data), headers=HEADERS,
                                                    timeout=self._timeout)

            return Response.parse(json_decoder(await response.read()), request)
        except json.decoder.JSONDecodeError as e:
            raise RocketgramParseError(e)
        except asyncio.CancelledError:
            raise
        except Exception as e:
            raise RocketgramNetworkError(e)
