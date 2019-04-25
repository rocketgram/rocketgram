# Copyright (C) 2015-2019 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from .base import BaseDispatcher


class BaseDispatcherProxy(BaseDispatcher):
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

    async def process(self):
        """Process new request."""

        raise NotImplementedError
