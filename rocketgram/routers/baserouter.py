# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).


import typing

if typing.TYPE_CHECKING:
    from ..bot import Bot


class BaseRouter:
    async def init(self, bot: 'Bot'):
        raise NotImplementedError

    async def shutdown(self, bot: 'Bot'):
        raise NotImplementedError

    async def process(self):
        raise NotImplementedError
