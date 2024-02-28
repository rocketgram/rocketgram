# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


class Router:
    __slots__ = ()

    async def init(self):
        raise NotImplementedError

    async def shutdown(self):
        raise NotImplementedError

    async def process(self):
        raise NotImplementedError
