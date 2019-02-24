# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).


import typing

if typing.TYPE_CHECKING:
    from ..bot import Bot
    from ..context import Context


class BaseDispatcher:
    async def init(self, bot: 'Bot'):
        raise NotImplemented

    async def shutdown(self, bot: 'Bot'):
        raise NotImplemented

    async def process(self, ctx: 'Context'):
        raise NotImplemented
