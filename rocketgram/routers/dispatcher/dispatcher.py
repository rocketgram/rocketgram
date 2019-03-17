# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).


import asyncio
import inspect
import logging
import typing
from contextlib import suppress

from .base import Waiter, WaitNext, BaseDispatcher
from .filters import FILTERS_ATTR, WAITER_ASSIGNED_ATTR
from ...update import UpdateType

if typing.TYPE_CHECKING:
    from ...context import Context
    from ...bot import Bot

logger = logging.getLogger('rocketgram.dispatcher')

SCOPE = '%s-%s-%s'


class HandlerNotFoundError(Exception):
    pass


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
    def __init__(self):
        super().__init__()

        self.__waiters: typing.Dict[str, Waiter] = dict()

        # TODO: Set waitings cleaner threshold.

    # def from_proxy(self, proxy: DispatcherProxy):
    #     for h in proxy.inits(self):
    #         self._init.append(h)
    #
    #     for h in proxy.shutdowns(self):
    #         self._shutdown.append(h)
    #
    #     for h in proxy.handlers(self):
    #         self._handlers.append(h)
    #
    #     for h in proxy.preprocessors(self):
    #         self._preprocessors.append(h)
    #
    #     for h in proxy.postprocessors(self):
    #         self._postprocessors.append(h)

    async def init(self, bot: 'Bot'):
        logger.debug('Performing init...')

        # sorting handlers by priority
        self._handlers = sorted(self._handlers, key=lambda handler: handler.priority)
        self._preprocessors = sorted(self._preprocessors, key=lambda handler: handler.priority)
        self._postprocessors = sorted(self._postprocessors, key=lambda handler: handler.priority)

        for func in self._init:
            await func(self, bot)

    async def shutdown(self, bot: 'Bot'):
        logger.debug('Performing shutdown...')
        for func in reversed(self._shutdown):
            await func(self, bot)

    async def process(self, ctx: 'Context'):
        """Process new request."""

        print(self.__waiters)
        print(_user_scope(ctx))

        try:
            handler = None
            anext = False

            # if have user scope, try find handler that wait continue
            # processing through async generators mechanism.

            # Run preprocessors...
            for pre in self._preprocessors:
                r = True
                for f in pre.filters:
                    if not await _call_or_await(f.func, ctx, *f.args, **f.kwargs):
                        r = False
                        break
                if r:
                    await pre.handler(ctx)

            scope = _user_scope(ctx)
            if scope and scope in self.__waiters:
                w = self.__waiters[scope]

                r = True
                filters = getattr(w.waiter, FILTERS_ATTR)
                for f in filters:
                    if not await _call_or_await(f.func, ctx, *f.args, **f.kwargs):
                        r = False
                        break

                if r and not await _call_or_await(w.waiter, ctx):
                    r = False

                if r:
                    handler = w
                    anext = True

            # Find handler from all handlers list.
            if handler is None:
                for h in self._handlers:
                    r = True
                    for f in h.filters:
                        if not await _call_or_await(f.func, ctx, *f.args, **f.kwargs):
                            r = False
                            break
                    if r:
                        handler = h
                        break

            # No handlers found. Exiting.
            if handler is None:
                raise HandlerNotFoundError()

            # If handler is async  generator...
            if inspect.isasyncgenfunction(handler.handler) or inspect.isasyncgen(handler.handler):
                wait = None
                with suppress(StopAsyncIteration):
                    if not anext:
                        gen = handler.handler(ctx)
                        wait = await gen.asend(None)
                    else:
                        gen = handler.handler
                        wait = await gen.asend(ctx)

                if not scope:
                    emsg = 'Got WaitNext from handler `%s` while user_scope' \
                           'is undefined for update %s' % (gen.__name__, ctx.update.update_id)
                    raise TypeError(emsg)

                if wait and not isinstance(wait, WaitNext):
                    emsg = 'Handler `%s` sends `%s` while WaitNext is expected!' % (gen.__name__, type(wait))
                    raise TypeError(emsg)

                if wait and not hasattr(wait.waiter, WAITER_ASSIGNED_ATTR):
                    emsg = 'Handler `%s` sends waiting function not registered as waiter!' % handler.handler.__name__
                    raise TypeError(emsg)

                # Check if waiter for scope already exist
                if scope in self.__waiters and self.__waiters[scope].handler != gen:
                    logger.warning('Overriding old wait in `%s` by `%s`d handler for update %s.',
                                   self.__waiters[scope].handler.__name__, gen.__name__, ctx.update.update_id)
                    await self.__waiters[scope].handler.aclose()

                # If new wait exist set it for scope otherwise remove scope from waiters
                if wait is not None:
                    self.__waiters[scope] = Waiter(gen, wait.waiter)
                elif scope in self.__waiters:
                    del self.__waiters[scope]

            # This is normal handler.
            else:
                r = handler.handler(ctx)
                if inspect.isawaitable(r):
                    await r

            # Run postprocessors...
            for post in self._preprocessors:
                r = True
                for f in post.filters:
                    if not await _call_or_await(f.func, ctx, *f.args, **f.kwargs):
                        r = False
                        break
                if r:
                    await post.handler(ctx)

        # except StopRequest:
        #     # TODO!
        except HandlerNotFoundError:
            logger.warning('Handler not found for update %s', ctx.update.update_id)
        except:
            logger.exception('Got exception during processing request')
