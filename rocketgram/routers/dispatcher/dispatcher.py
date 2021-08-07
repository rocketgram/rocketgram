# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


import asyncio
import logging
import typing
from contextlib import suppress
from dataclasses import dataclass, replace
from inspect import isawaitable, isasyncgenfunction, isasyncgen
from time import time
from typing import Tuple, List, Dict, Callable, Coroutine, AsyncGenerator, Union

from .base import BaseDispatcher, DEFAULT_PRIORITY, _call_or_await
from .filters import FilterParams, WAITER_ASSIGNED_ATTR
from .waiters import WaitNext, DropWaiter
from ...api import UpdateType
from ...context import context

logger = logging.getLogger('rocketgram.dispatcher')

DEFAULT_WATIRES_LIFETIME = 60 * 60 * 24  # 1 day
DEFAULT_WATIRES_LIFETIME_CHECK = 60 * 30  # 30 minutes


class HandlerNotFoundError(Exception):
    pass


@dataclass(frozen=True)
class Waiter:
    created: int
    handler: Union[Callable, Coroutine, AsyncGenerator]
    waiter: Union[Callable, Coroutine]
    args: Tuple
    kwargs: Dict
    filters: List[FilterParams]


def _user_scope():
    """Finds user scope for waits.

    Valid user scope can be only for message or callback query in chats and groups."""

    if context.update.type == UpdateType.message:
        return f"{id(context.bot)}-{context.chat.id}-{context.user.id}"
    if context.update.type == UpdateType.callback_query:
        if context.message is None:
            return None
        return f"{id(context.bot)}-{context.chat.id}-{context.user.id}"


async def _run_filters(filters):
    for filt in filters:
        fr = await _call_or_await(filt.func, *filt.args, **filt.kwargs)
        assert isinstance(fr, bool), \
            f'Filter `{filt.func.__name__}` returns `{type(fr)}` while `bool` is expected!'
        if not fr:
            return False

    return True


class Dispatcher(BaseDispatcher):
    __slots__ = ('__waiters', '__watires_lifetime', '__watires_lifetime_check', '__last_waiters_check')

    def __init__(self, *, default_priority=DEFAULT_PRIORITY,
                 watires_lifetime=DEFAULT_WATIRES_LIFETIME,
                 watires_lifetime_check=DEFAULT_WATIRES_LIFETIME_CHECK):
        super().__init__(default_priority=default_priority)

        self.__waiters: typing.Dict[str, Waiter] = dict()
        self.__watires_lifetime = watires_lifetime
        self.__watires_lifetime_check = watires_lifetime_check
        self.__last_waiters_check = int(time())

    async def __find_waiter(self, scope):
        if scope not in self.__waiters:
            return

        waiter = self.__waiters[scope]

        if not await _run_filters(waiter.filters):
            return
        wr = await _call_or_await(waiter.waiter, *waiter.args, **waiter.kwargs)

        assert isinstance(wr, bool), \
            f'Waiter `{waiter.waiter.__name__}` returns `{type(wr)}` while `bool` is expected!'

        if not wr:
            return

        return waiter

    async def __run_generator(self, anext: bool, handler, scope):
        wait = None  # noqa

        with suppress(StopAsyncIteration):
            gen = handler.handler
            if not anext:
                gen = gen()
            wait = await gen.asend(None)

        assert not (wait and not isinstance(wait, (WaitNext, DropWaiter))), \
            f'Handler `{gen.__name__}` sends `{type(wait)}` while WaitNext or DropWaiter is expected!'

        if isinstance(wait, DropWaiter):
            # drop current waiter
            if scope in self.__waiters:
                with suppress(StopAsyncIteration):
                    await self.__waiters[scope].handler.aclose()
                del self.__waiters[scope]

            # re-run generator again
            await self.__run_generator(True, Waiter(int(time()), gen, lambda: True, (), {}, []), scope)
            return

        assert not (wait and not hasattr(wait.waiter, WAITER_ASSIGNED_ATTR)), \
            f'Handler `{handler.handler.__name__}` sends waiting function not registered as waiter!'

        # Check if other waiter for scope already exist
        if scope in self.__waiters and self.__waiters[scope].handler != gen:
            logger.warning('Overriding old wait in `%s` by `%s` handler for update %s.',
                           self.__waiters[scope].handler.__name__, gen.__name__, context.update.update_id)
            with suppress(StopAsyncIteration):
                await self.__waiters[scope].handler.aclose()

        # If new wait exist set it for scope otherwise remove scope from waiters
        if wait is not None:
            self.__waiters[scope] = Waiter(int(time()), gen, wait.waiter, wait.args, wait.kwargs, wait.filters)
        elif scope in self.__waiters:
            del self.__waiters[scope]

    async def process(self):
        """Process new request."""

        try:
            # Run preprocessors...
            for pre in self._pre:
                if await _run_filters(pre.filters):
                    await _call_or_await(pre.handler)

            anext = False
            scope = _user_scope()
            handler = None

            # if have user scope, try find handler that wait continue
            # processing through async generators mechanism.
            if scope:
                handler = await self.__find_waiter(scope)
            if handler:
                anext = True

            # Find handler from handlers list.
            if not handler:
                for hdlr in self._handlers:
                    if await _run_filters(hdlr.filters):
                        handler = hdlr
                        break

            # No handlers found. Exiting.
            if not handler:
                raise HandlerNotFoundError

            # Run handler...
            if isasyncgenfunction(handler.handler) or isasyncgen(handler.handler):
                # handler is async generator...
                if not scope:
                    emsg = f'Found async generator `{handler.handler.__name__}` but user_scope' \
                           f'is undefined for update `{context.update.update_id}`'
                    raise TypeError(emsg)
                await self.__run_generator(anext, handler, scope)
            else:
                # This is normal handler.
                r = handler.handler()
                if isawaitable(r):
                    await r

            # Run postprocessors...
            for post in self._post:
                if await _run_filters(post.filters):
                    await _call_or_await(post.handler)

            # Cleanup waiters:
            current = int(time())
            if current > self.__last_waiters_check + self.__watires_lifetime_check:
                self.__last_waiters_check = current
                _ = asyncio.create_task(self.__waiters_cleanup(current))

        except HandlerNotFoundError:
            logger.warning('Handler not found for update:\n%s', replace(context.update, raw=dict()))

    async def __waiters_cleanup(self, current: int):
        closes = list()
        for k in list(self.__waiters.keys()):
            wtr = self.__waiters[k]
            if current - wtr.created > self.__watires_lifetime:
                del self.__waiters[k]
                closes.append(wtr)
        for cl in closes:
            with suppress(StopAsyncIteration):
                await cl.handler.aclose()
