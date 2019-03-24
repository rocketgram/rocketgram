# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).


import asyncio
import logging

import aiohttp

try:
    import ujson as json
except ModuleNotFoundError:
    import json

from .. import types
from .baseconnector import BaseConnector
from ..requests import Request
from ..update import Response
from ..errors import RocketgramNetworkError, RocketgramParseError

logger = logging.getLogger('rocketgram.connectors.aiohttpconnector')


class AioHttpConnector(BaseConnector):
    def __init__(self, loop: asyncio.AbstractEventLoop = None, timeout: int = 30,
                 api_url: str = types.API_URL):
        if not loop:
            loop = asyncio.get_event_loop()
        self._api_url = api_url
        self._session = aiohttp.ClientSession(loop=loop)
        self._timeout = timeout

    async def init(self):
        pass

    async def shutdown(self):
        await self._session.close()

    async def send(self, token: str, request: Request) -> Response:
        try:
            url = self._api_url % token + request.method

            request_data = request.render()
            send_file = False
            data = dict()
            for k, v in request_data.items():
                if v is not None:
                    data[k] = v
                if isinstance(v, types.InputFile):
                    send_file = True

            if send_file:
                data = aiohttp.FormData()
                for name, field in request_data.items():
                    if isinstance(field, types.InputFile):
                        data.add_field(name, field.file, filename=field.file_name, content_type=field.content_type)
                    elif isinstance(field, dict) or isinstance(field, list):
                        data.add_field(name, json.dumps(field), content_type='application/json')
                    else:
                        data.add_field(name, str(field), content_type='text/plain')
                response = await self._session.post(url, data=data, timeout=self._timeout)
            else:
                headers = {'Content-Type': 'application/json'}
                response = await self._session.post(url, data=json.dumps(request_data), headers=headers, timeout=self._timeout)

            return Response.parse(json.loads(await response.read()), request)
        except json.decoder.JSONDecodeError as e:
            raise RocketgramParseError(e)
        except Exception as e:
            raise RocketgramNetworkError(e)
