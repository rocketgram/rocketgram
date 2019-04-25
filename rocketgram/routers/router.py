# Copyright (C) 2015-2019 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


import typing

if typing.TYPE_CHECKING:
    from ..bot import Bot


class Router:
    async def init(self):
        raise NotImplementedError

    async def shutdown(self):
        raise NotImplementedError

    async def process(self):
        raise NotImplementedError
