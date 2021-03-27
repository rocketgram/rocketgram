# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


import asyncio
import logging
from json import JSONDecodeError

import aiohttp

from .connector import Connector
from ..api import Request, Response
from ..errors import RocketgramNetworkError, RocketgramParseError

try:
    import ujson as json
except ImportError:
    import json

logger = logging.getLogger('rocketgram.connectors.aiohttp')


class AioHttpConnector(Connector):
    __slots__ = ('_api_url', '_api_file_url', '_session', '_timeout')

    def __init__(self, *, timeout: int = 35, api_url: str = Connector.API_URL,
                 api_file_url: str = Connector.API_FILE_URL):
        super().__init__(timeout=timeout, api_url=api_url, api_file_url=api_file_url)
        self._session = aiohttp.ClientSession(loop=asyncio.get_event_loop())

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
                data = aiohttp.FormData(quote_fields=False)
                for name, field in request_data.items():
                    if isinstance(field, (dict, list, tuple)):
                        data.add_field(name, json.dumps(field), content_type='application/json')
                        continue
                    data.add_field(name, str(field), content_type='text/plain')

                for file in files:
                    data.add_field(file.file_name, file.data, filename=file.file_name, content_type=file.content_type)

                response = await self._session.post(url, data=data, timeout=self._timeout)
            else:
                response = await self._session.post(url, data=json.dumps(request_data), headers=self.HEADERS,
                                                    timeout=self._timeout)

            return Response.parse(json.loads(await response.read()), request)
        except JSONDecodeError as e:
            raise RocketgramParseError(e)
        except asyncio.CancelledError:
            raise
        except Exception as error:
            raise RocketgramNetworkError(error) from error
