# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


import asyncio
import logging
from dataclasses import dataclass
from inspect import isclass
from typing import Callable, Coroutine, AsyncGenerator, Union, List

from .filters import FILTERS_ATTR, PRIORITY_ATTR, WAITER_ASSIGNED_ATTR, HANDLER_ASSIGNED_ATTR
from .filters import FilterParams, _check_sig
from ..router import Router
from ... import bot
from ...context import context

logger = logging.getLogger('rocketgram.dispatcher')


@dataclass
class Handler:
    priority: int
    handler: Union[Callable, Coroutine, AsyncGenerator]
    filters: List[FilterParams]


DEFAULT_PRIORITY = 1024


def _get_function(handler):
    if not isclass(handler):
        return handler

    instance = handler()
    assert callable(instance), "Class handlers must be callable!"
    return instance


async def _call_or_await(func, *args, **kwargs):
    r = func(*args, **kwargs)
    if asyncio.iscoroutine(r):
        return await r
    return r


class BaseDispatcher(Router):
    __slots__ = ('_init', '_shutdown', '_handlers', '_pre', '_post', '_default_priority', '_bots')

    def __init__(self, *, default_priority=DEFAULT_PRIORITY):
        self._init = list()
        self._shutdown = list()
        self._handlers: List[Handler] = list()
        self._pre: List[Handler] = list()
        self._post: List[Handler] = list()
        self._default_priority = default_priority
        self._bots: List['bot.Bot'] = list()

    @property
    def default_priority(self):
        return self._default_priority

    def _resort_handlers(self):
        # sorting handlers by priority
        self._handlers = sorted(self._handlers, key=lambda handler: handler.priority)
        self._pre = sorted(self._pre, key=lambda handler: handler.priority)
        self._post = sorted(self._post, key=lambda handler: handler.priority)

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

    def from_dispatcher(self, dispatcher: 'BaseDispatcher'):
        self._init.extend(dispatcher.inits)
        self._shutdown.extend(dispatcher.shutdowns)
        self._handlers.extend(dispatcher.handlers)
        self._pre.extend(dispatcher.befores)
        self._post.extend(dispatcher.afters)

        # if handler added in runtime - resort handlers
        if len(self._bots):
            self._resort_handlers()

    async def init(self):
        logger.debug('Performing init...')

        if not len(self._bots):
            self._resort_handlers()

        self._bots.append(context.bot)

        for func in self._init:
            await _call_or_await(func)

    async def shutdown(self):
        logger.debug('Performing shutdown...')

        for func in reversed(self._shutdown):
            await _call_or_await(func)

        self._bots.remove(context.bot)

    def on_init(self, func):
        """Registers init"""

        self._init.append(func)
        return func

    def on_shutdown(self, func):
        """Registers shutdown"""

        self._shutdown.append(func)
        return func

    def _register(self, what: List[Handler], handler: Callable[..., None]):
        # Save handler to given handlers list.

        function = _get_function(handler)

        assert _check_sig(function), \
            'Handler `%s` must not take any arguments!' % handler

        assert not hasattr(handler, HANDLER_ASSIGNED_ATTR), 'Handler already registered!'
        assert not hasattr(handler, WAITER_ASSIGNED_ATTR), 'Already registered as waiter!'

        priority = getattr(handler, PRIORITY_ATTR, self._default_priority)
        assert isinstance(priority, int), 'Handler function has wrong priority!'

        filters = getattr(handler, FILTERS_ATTR, list())
        assert isinstance(filters, list), 'Handler function has wrong filters!'
        assert len(filters), 'Handler must have at least one filter!'

        what.append(Handler(priority, function, filters))

        setattr(function, HANDLER_ASSIGNED_ATTR, True)

        # if handler added in runtime - resort handlers
        if len(self._bots):
            self._resort_handlers()

    def handler(self, handler: Callable[..., None]):
        """Registers handler"""

        self._register(self._handlers, handler)
        return handler

    def before(self, handler: Callable[..., None]):
        """Registers preprocessor"""

        self._register(self._pre, handler)
        return handler

    def after(self, handler: Callable[..., None]):
        """Registers postprocessor"""

        self._register(self._post, handler)
        return handler

    async def process(self):
        """Process new request."""

        raise NotImplementedError
