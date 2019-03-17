# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from inspect import signature
from typing import Callable, Coroutine, AsyncGenerator, Union, Optional, List, TYPE_CHECKING

from .filters import FILTERS_ATTR, PRIORITY_ATTR, HANDLER_ASSIGNED_ATTR
from ..baserouter import BaseRouter

if TYPE_CHECKING:
    from ...context import Context

__all__ = ['BaseDispatcher', 'WaitNext']


@dataclass
class Handler:
    priority: int
    handler: Union[Callable, Coroutine, AsyncGenerator]
    filters: Optional[Union[Callable, Coroutine]]


@dataclass
class Waiter:
    handler: Union[Callable, Coroutine, AsyncGenerator]
    waiter: Union[Callable, Coroutine]


@dataclass
class WaitNext:
    waiter: Union[Callable, Coroutine]


DEFAULT_PRIORITY = 1024


def _register(what: List[Handler], handler_func: Callable[['Context'], None]):
    # Checking calling signature for handler_func.
    try:
        sig = signature(handler_func)
        # object() means Context, passing to handler at runtime.
        sig.bind(object())
    except TypeError:
        es = 'Handler `%s` must take exactly one argument `ctx: Context`!' % handler_func.__name__
        raise TypeError(es) from None

    priority = getattr(handler_func, PRIORITY_ATTR, DEFAULT_PRIORITY)

    try:
        filters = getattr(handler_func, FILTERS_ATTR)
    except AttributeError:
        raise TypeError('Handler must have at least one filter!')

    # TODO: Check filter types!

    handler = Handler(priority, handler_func, filters)

    what.append(handler)

    setattr(handler_func, HANDLER_ASSIGNED_ATTR, True)
    return handler_func


class BaseDispatcher(BaseRouter):
    def __init__(self):
        self._init = list()
        self._shutdown = list()
        self._handlers: List[Handler] = list()
        self._preprocessors: List[Handler] = list()
        self._postprocessors: List[Handler] = list()

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

    def handler(self, handler_func: Callable[['Context'], None]):
        """Registers handler"""

        return _register(self._handlers, handler_func)

    def on_enter(self, handler_func: Callable[['Context'], None]):
        """Registers preprocessor"""

        return _register(self._preprocessors, handler_func)

    def on_leave(self, handler_func: Callable[['Context'], None]):
        """Registers postprocessor"""

        return _register(self._postprocessors, handler_func)
