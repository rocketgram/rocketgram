# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).

import logging
import typing

from ..requests import Request

if typing.TYPE_CHECKING:
    from ..bot import Bot

logger = logging.getLogger('rocketgram.executors.updates')


class Executor:
    @property
    def bots(self) -> typing.List['Bot']:
        raise NotImplementedError

    @property
    def running(self) -> bool:
        raise NotImplementedError

    def can_process_webhook_request(self, request: Request) -> bool:
        raise NotImplementedError

    async def add_bot(self, bot: 'Bot', *, drop_updates=False):
        raise NotImplementedError

    async def remove_bot(self, bot: 'Bot'):
        raise NotImplementedError

    async def start(self):
        raise NotImplementedError

    async def stop(self):
        raise NotImplementedError
