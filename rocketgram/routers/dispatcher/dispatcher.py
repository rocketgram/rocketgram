# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).

import asyncio
import inspect
import logging
import typing
from contextlib import suppress
from dataclasses import dataclass
from typing import List, Callable, Coroutine, AsyncGenerator, Union

from .base import BaseDispatcher, Handler, DEFAULT_PRIORITY
from .filters import WaitNext, FilterParams, WAITER_ASSIGNED_ATTR
from ...update import UpdateType

if typing.TYPE_CHECKING:
    from ...context import Context

logger = logging.getLogger('rocketgram.dispatcher')

SCOPE = '%s-%s-%s'


class StopRequest(Exception):
    pass


class HandlerNotFoundError(Exception):
    pass


@dataclass
class Waiter:
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


class Dispatcher(BaseDispatcher):
    def __init__(self, *, default_priority=DEFAULT_PRIORITY):
        super().__init__(default_priority=default_priority)

        self.__waiters: typing.Dict[str, Waiter] = dict()

        # TODO: Set waitings cleaner threshold.

    async def __find_waiter(self, ctx: 'Context', scope):
        if scope not in self.__waiters:
            return

        waiter = self.__waiters[scope]

        for f in waiter.filters:
            if not await _call_or_await(f.func, ctx, *f.args, **f.kwargs):
                return

        if not await _call_or_await(waiter.waiter, ctx):
            return

        return waiter

    async def __find_handler(self, ctx: 'Context'):
        for handler in self._handlers:
            r = True
            for f in handler.filters:
                if not await _call_or_await(f.func, ctx, *f.args, **f.kwargs):
                    r = False
                    break
            if r:
                return handler

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
            self.__waiters[scope] = Waiter(gen, wait.waiter, wait.filters)
        elif scope in self.__waiters:
            del self.__waiters[scope]

    async def __run_prepost(self, ctx: 'Context', prepost: List[Handler]):
        for pre in prepost:
            r = True
            for f in pre.filters:
                if not await _call_or_await(f.func, ctx, *f.args, **f.kwargs):
                    r = False
                    break
            if r:
                await pre.handler(ctx)

    async def process(self, ctx: 'Context'):
        """Process new request."""

        try:
            # Run preprocessors...
            await self.__run_prepost(ctx, self._pre)

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
                handler = await self.__find_handler(ctx)

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
            await self.__run_prepost(ctx, self._post)

        except StopRequest as e:
            logger.debug('Request was %s interrupted: %s', ctx.update.update_id, e)
        except HandlerNotFoundError:
            logger.warning('Handler not found for update %s', ctx.update.update_id)
        except:
            logger.exception('Got exception during processing request')
