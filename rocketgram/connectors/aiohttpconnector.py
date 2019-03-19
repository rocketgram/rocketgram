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
from .baseconnector import BaseConnector, Response
from ..errors import TelegramConnectionError, TelegramTimeoutError, TelegramParseError

logger = logging.getLogger('rocketgram.connectors.aiohttpconnector')


class AioHttpConnector(BaseConnector):
    def __init__(self, loop: asyncio.AbstractEventLoop = None, timeout: int = 0):
        super().__init__(loop)
        self._session = aiohttp.ClientSession(loop=self._loop)
        self._timeout = timeout

    async def init(self):
        pass

    async def shutdown(self):
        await self._session.close()

    async def send(self, url: str, data: dict):
        headers = {'Content-Type': 'application/json'}

        try:
            response = await self._session.post(url, data=json.dumps(data), headers=headers, timeout=self._timeout)
            return Response(response.status, json.loads(await response.read()))
        except aiohttp.ClientConnectionError:
            raise TelegramConnectionError
        except aiohttp.ServerTimeoutError:
            raise TelegramTimeoutError
        except json.decoder.JSONDecodeError:
            raise TelegramParseError

    async def send_file(self, url: str, data: dict):
        d = aiohttp.FormData()

        for name, field in data.items():
            if isinstance(field, types.InputFile):
                d.add_field(name, field.file, filename=field.file_name, content_type=field.content_type)
            elif isinstance(field, dict) or isinstance(field, list):
                d.add_field(name, json.dumps(field), content_type='application/json')
            else:
                d.add_field(name, str(field), content_type='text/plain')

        try:
            response = await self._session.post(url, data=d, timeout=self._timeout)
            return Response(response.status, json.loads(await response.read()))
        except aiohttp.ClientConnectionError:
            raise TelegramConnectionError
        except aiohttp.ServerTimeoutError:
            raise TelegramTimeoutError
        except json.decoder.JSONDecodeError:
            raise TelegramParseError
