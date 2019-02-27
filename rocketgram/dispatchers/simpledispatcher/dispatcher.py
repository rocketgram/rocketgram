# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).


import asyncio
import inspect
import logging
import typing
from contextlib import suppress

from .base import Handler, WaitNext, BaseSimpleDispatcher
from .proxy import SimpleDispatcherProxy
from ...update import UpdateType

if typing.TYPE_CHECKING:
    from ...context import Context
    from ...bot import Bot

logger = logging.getLogger('rocketgram.simpledispatcher')

SCOPE = '%s-%s-%s'


class HandlerNotFoundError(Exception):
    pass


async def _call_or_await(callable, *args, **kwargs):
    r = callable(*args, **kwargs)
    if asyncio.iscoroutine(r):
        return await r
    return r


class SimpleDispatcher(BaseSimpleDispatcher):
    def __init__(self):
        super().__init__()

        self.__waitings = dict()

    def from_proxy(self, proxy: SimpleDispatcherProxy):
        for h in proxy.inits(self):
            self._init.append(h)

        for h in proxy.shutdowns(self):
            self._shutdown.append(h)

        for h in proxy.handlers(self):
            self._handlers.append(h)

        for h in proxy.preprocessors(self):
            self._preprocessors.append(h)

        for h in proxy.postprocessors(self):
            self._postprocessors.append(h)

    async def init(self, bot: 'Bot'):
        logger.debug('Performing init...')
        for func in self._init:
            await func(self, bot)

    async def shutdown(self, bot: 'Bot'):
        logger.debug('Performing shutdown...')
        for func in reversed(self._shutdown):
            await func(self, bot)

    async def __run_handler(self, ctx, handler: Handler, anext=False):
        r = handler.handler(ctx)

        if asyncio.iscoroutine(handler.handler):
            await r
            return

        if inspect.isasyncgen(r):
            param = ctx if anext else None
            wn = await g.asend(param)

            if not isinstance(wn, WaitNext):
                return None

            return wn

    def __user_scope(self, ctx):
        """Finds user scope for waits.

        Valid user scope can be only for message or callback query in chats and groups."""

        if ctx.update.update_type == UpdateType.message:
            return SCOPE % (id(ctx.bot), ctx.update.message.chat.chat_id, ctx.update.message.user.user_id)
        elif ctx.update.update_type == UpdateType.callback_query:
            if ctx.update.callback_query.inline_message_id is not None:
                return None
            return SCOPE % (
                id(ctx.bot), ctx.update.callback_query.message.chat.chat_id,
                ctx.update.callback_query.message.user.user_id)

    async def process(self, ctx: 'Context'):
        """Process new request."""
        try:

            handler = None
            anext = False

            # if have user scope, try find handler that wait continue
            # processing through async generators mechanism.

            scope = self.__user_scope(ctx)
            print('user_scope', scope)
            if scope and scope in self.__waitings:
                h = self.__waitings[scope]
                filter_result = await _call_or_await(h.filter, ctx)
                if filter_result:
                    handler = h
                    anext = True

            # Find valid handler from all handlers list.
            if handler is None:
                for h in self._handlers:
                    filter_result = await _call_or_await(h.filter, ctx)
                    if filter_result:
                        handler = h
                        break

            # No handlers found. Exiting.
            if handler is None:
                raise HandlerNotFoundError()

            # Run preprocessors
            for pre in self._preprocessors:
                filter_result = await _call_or_await(pre.filter, ctx)
                if filter_result:
                    await pre.handler(ctx)

            if inspect.isasyncgenfunction(handler.handler) or inspect.isasyncgen(handler.handler):
                if not anext:
                    gen = handler.handler(ctx)
                    wait = await gen.asend(None)
                else:
                    gen = handler.handler
                    wait = None
                    with suppress(StopAsyncIteration):
                        wait = await gen.asend(ctx)

                print(wait)

                if not scope:
                    raise TypeError('Got WaitNext while user_scope is undefined for update %s' % ctx.update.update_id)
                if wait and not isinstance(wait, WaitNext):
                    raise TypeError('Generator returns %s while WaitNext is expected' % type(wait))

                if scope in self.__waitings and self.__waitings[scope].handler != gen:
                    logger.warning('Overriding old wait %s by %s handler for update %s. This may me error.',
                                   self.__waitings[scope].handler, gen, ctx.update.update_id)
                    await self.__waitings[scope].handler.aclose()
                if wait:
                    filter = wait.filter if wait.filter else lambda ctx: True
                    self.__waitings[scope] = Handler(gen, filter, wait.forward)
                elif scope in self.__waitings:
                    del self.__waitings[scope]
            else:
                r = handler.handler(ctx)
                if inspect.isawaitable(r):
                    await r

            for post in self._postprocessors:
                filter_result = await _call_or_await(post.filter, ctx)
                if filter_result:
                    await post.handler(ctx)

        except HandlerNotFoundError:
            logger.warning('Handler not found for update %s', ctx.update.update_id)
        except:
            logger.exception('Got exception during processing request')
