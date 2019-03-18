# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).

import asyncio
import inspect
import logging
import typing
from contextlib import suppress
from dataclasses import dataclass
from time import time
from typing import List, Callable, Coroutine, AsyncGenerator, Union

from .base import BaseDispatcher, DEFAULT_PRIORITY
from .filters import WaitNext, FilterParams, WAITER_ASSIGNED_ATTR
from ...update import UpdateType

if typing.TYPE_CHECKING:
    from ...context import Context

logger = logging.getLogger('rocketgram.dispatcher')

SCOPE = '%s-%s-%s'

DEFAULT_WATIRES_LIFETIME = 60 * 60 * 24  # 1 day
DEFAULT_WATIRES_LIFETIME_CHECK = 60 * 30  # 30 minutes


class StopRequest(Exception):
    pass


class HandlerNotFoundError(Exception):
    pass


@dataclass
class Waiter:
    created: int
    handler: Union[Callable, Coroutine, AsyncGenerator]
    waiter: Union[Callable, Coroutine]
    filters: List[FilterParams]


async def _call_or_await(func, *args, **kwargs):
    r = func(*args, **kwargs)
    if asyncio.iscoroutine(r):
        return await r
    return r


def _user_scope(ctx: 'Context'):
    """Finds user scope for waits.

    Valid user scope can be only for message or callback query in chats and groups."""

    if ctx.update.update_type == UpdateType.message:
        return SCOPE % (id(ctx.bot), ctx.update.message.chat.chat_id, ctx.update.message.user.user_id)
    elif ctx.update.update_type == UpdateType.callback_query:
        if ctx.update.callback_query.message is None:
            return None
        return SCOPE % (id(ctx.bot),
                        ctx.update.callback_query.message.chat.chat_id,
                        ctx.update.callback_query.user.user_id)


async def _run_filters(ctx, filters):
    for fltr in filters:
        fr = await _call_or_await(fltr.func, ctx, *fltr.args, **fltr.kwargs)
        assert isinstance(fr, bool), \
            'Filter `%s` returns `%s` while `bool` is expected!' % (fltr.func.__name__, type(fr))
        if not fr:
            return False

    return True


class Dispatcher(BaseDispatcher):
    def __init__(self, *, default_priority=DEFAULT_PRIORITY,
                 watires_lifetime=DEFAULT_WATIRES_LIFETIME,
                 watires_lifetime_check=DEFAULT_WATIRES_LIFETIME_CHECK):
        super().__init__(default_priority=default_priority)

        self.__waiters: typing.Dict[str, Waiter] = dict()
        self.__watires_lifetime = watires_lifetime
        self.__watires_lifetime_check = watires_lifetime_check
        self.__last_waiters_check = int(time())

    async def __find_waiter(self, ctx: 'Context', scope):
        if scope not in self.__waiters:
            return

        waiter = self.__waiters[scope]

        if not await _run_filters(ctx, waiter.filters):
            return
        wr = await _call_or_await(waiter.waiter, ctx)

        assert isinstance(wr, bool), \
            'Waiter `%s` returns `%s` while `bool` is expected!' % (waiter.waiter.__name__, type(wr))

        if not wr:
            return

        return waiter

    async def __run_generator(self, anext: bool, ctx, handler, scope):
        wait = None

        with suppress(StopAsyncIteration):
            if not anext:
                gen = handler.handler(ctx)
                wait = await gen.asend(None)
            else:
                gen = handler.handler
                wait = await gen.asend(ctx)

        assert not (wait and not isinstance(wait, WaitNext)), \
            'Handler `%s` sends `%s` while WaitNext is expected!' % (gen.__name__, type(wait))

        assert not (wait and not hasattr(wait.waiter, WAITER_ASSIGNED_ATTR)), \
            'Handler `%s` sends waiting function not registered as waiter!' % handler.handler.__name__

        # Check if other waiter for scope already exist
        if scope in self.__waiters and self.__waiters[scope].handler != gen:
            logger.warning('Overriding old wait in `%s` by `%s` handler for update %s.',
                           self.__waiters[scope].handler.__name__, gen.__name__, ctx.update.update_id)
            await self.__waiters[scope].handler.aclose()

        # If new wait exist set it for scope otherwise remove scope from waiters
        if wait is not None:
            self.__waiters[scope] = Waiter(int(time()), gen, wait.waiter, wait.filters)
        elif scope in self.__waiters:
            del self.__waiters[scope]

    async def process(self, ctx: 'Context'):
        """Process new request."""

        try:
            # Run preprocessors...
            for pre in self._pre:
                if await _run_filters(ctx, pre.filters):
                    await pre.handler(ctx)

            anext = False
            scope = _user_scope(ctx)
            handler = None

            # if have user scope, try find handler that wait continue
            # processing through async generators mechanism.
            if scope:
                handler = await self.__find_waiter(ctx, scope)
            if handler:
                anext = True

            # Find handler from handlers list.
            if not handler:
                for hdlr in self._handlers:
                    if await _run_filters(ctx, hdlr.filters):
                        handler = hdlr
                        break

            # No handlers found. Exiting.
            if not handler:
                raise HandlerNotFoundError()

            # Run handler...
            if inspect.isasyncgenfunction(handler.handler) or inspect.isasyncgen(handler.handler):
                # handler is async generator...
                if not scope:
                    emsg = 'Found async generatro `%s` but user_scope' \
                           'is undefined for update %s' % (handler.handler.__name__, ctx.update.update_id)
                    raise TypeError(emsg)
                await self.__run_generator(anext, ctx, handler, scope)
            else:
                # This is normal handler.
                r = handler.handler(ctx)
                if inspect.isawaitable(r):
                    await r

            # Run postprocessors...
            for post in self._post:
                if await _run_filters(ctx, post.filters):
                    await post.handler(ctx)

            # Cleanup waiters:
            current = int(time())
            if current > self.__last_waiters_check + self.__watires_lifetime_check:
                self.__last_waiters_check = current
                _ = asyncio.create_task(self.__waiters_cleanup(current))

        except StopRequest as e:
            logger.debug('Request was %s interrupted: %s', ctx.update.update_id, e)
        except HandlerNotFoundError:
            logger.warning('Handler not found for update %s', ctx.update.update_id)
        except:
            logger.exception('Got exception during processing request')

    async def __waiters_cleanup(self, current: int):
        closes = list()
        for k in self.__waiters.keys():
            wtr = self.__waiters[k]
            if current - wtr.created > self.__watires_lifetime:
                del self.__waiters[k]
                closes.append(wtr.handler.aclose())
        for cl in closes:
            with suppress(StopAsyncIteration):
                await cl
