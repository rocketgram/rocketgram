# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).


import typing
from dataclasses import dataclass

from ..basedispatcher import BaseDispatcher

if typing.TYPE_CHECKING:
    from ...bot import Bot
    from ...context import Context


@dataclass
class Handler:
    handler: typing.Union[typing.Callable, typing.Awaitable, typing.AsyncGenerator]
    filter: typing.Optional[typing.Union[typing.Callable, typing.Awaitable]]
    forward: bool


@dataclass
class WaitNext:
    filter: typing.Optional[typing.Union[typing.Callable, typing.Awaitable]]
    forward: bool


@dataclass
class FilterResult:
    args: typing.Optional[typing.Union[typing.List, typing.Tuple]]


class BaseSimpleDispatcher(BaseDispatcher):
    def __init__(self):
        self._init = list()
        self._shutdown = list()
        self._handlers: typing.List[Handler] = list()
        self._preprocessors: typing.List[Handler] = list()
        self._postprocessors: typing.List[Handler] = list()

    async def init(self, bot: 'Bot'):
        raise NotImplemented

    async def shutdown(self, bot: 'Bot'):
        raise NotImplemented

    async def process(self, ctx: 'Context'):
        raise NotImplemented

    def on_init(self):
        """Registers init"""

        def internal(func):
            self._init.append(func)
            return func

        return internal

    def on_shutdown(self):
        """Registers shutdown"""

        def internal(func):
            self._shutdown.append(func)
            return func

        return internal

    def on_update(self, filter: typing.Callable = None, *, forward=True):
        """Registers handler"""

        if filter is None:
            filter = lambda ctx: True

        def _int(func: typing.Coroutine):
            self._handlers.append(Handler(func, filter, forward))

            return func

        return _int

    def on_enter(self, filter: typing.Callable = None, *, forward=True):
        """Registers preprocessor"""

        if filter is None:
            filter = lambda ctx: True

        def _int(func: typing.Coroutine):
            self._preprocessors.append(Handler(func, filter, forward))

            return func

        return _int

    def on_leave(self, filter: typing.Union[typing.Callable, typing.Awaitable] = None, *, forward=True):
        """Registers postprocessor"""

        if filter is None:
            filter = lambda ctx: True

        def _int(func: typing.Coroutine):
            self._postprocessors.append(Handler(func, filter, forward))

            return func

        return _int
