# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).


from typing import TYPE_CHECKING

from .base import BaseDispatcher

if TYPE_CHECKING:
    from ...context import Context


class DispatcherProxy(BaseDispatcher):
    @property
    def inits(self):
        return self._init

    @property
    def shutdowns(self):
        return self._shutdown

    @property
    def handlers(self):
        return self._handlers

    @property
    def befores(self):
        return self._pre

    @property
    def afters(self):
        return self._post

    async def process(self, ctx: 'Context'):
        """Process new request."""

        raise NotImplementedError
