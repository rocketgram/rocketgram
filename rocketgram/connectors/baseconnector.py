# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).


import asyncio
import logging
from collections import namedtuple

logger = logging.getLogger('rocketgram.connectors.baseconnector')

Response = namedtuple('Response', ('status', 'data'))


class BaseConnector():
    def __init__(self, loop: asyncio.AbstractEventLoop = None):
        if not loop:
            loop = asyncio.get_event_loop()

        self._loop = loop

    async def init(self):
        raise NotImplementedError

    async def shutdown(self):
        raise NotImplementedError

    async def send(self, url: str, data):
        raise NotImplementedError

    async def send_file(self, url: str, data):
        raise NotImplementedError
