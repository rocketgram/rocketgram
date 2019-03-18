# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).

import logging
import typing

if typing.TYPE_CHECKING:
    from ..bot import Bot

logger = logging.getLogger('rocketgram.executors.updates')


class Executor:
    def __init__(self):
        raise NotImplemented

    @property
    def bots(self) -> typing.List['Bot']:
        raise NotImplemented

    @property
    def running(self) -> bool:
        raise NotImplemented

    async def add_bot(self, bot: 'Bot', *, drop_updates=False):
        raise NotImplemented

    async def remove_bot(self, bot: 'Bot'):
        raise NotImplemented

    async def start(self):
        raise NotImplemented

    async def stop(self):
        raise NotImplemented
