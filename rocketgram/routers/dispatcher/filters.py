# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from functools import wraps
from inspect import signature
from typing import List, Union, Callable, Coroutine, Tuple, Dict, TYPE_CHECKING

FILTERS_ATTR = 'rocketgram_dispatcher_filters'
PRIORITY_ATTR = 'rocketgram_dispatcher_handler_priority'
HANDLER_ASSIGNED_ATTR = 'rocketgram_dispatcher_handler_assigned'
WAITER_ASSIGNED_ATTR = 'rocketgram_dispatcher_waiter_assigned'

if TYPE_CHECKING:
    from ...context import Context


@dataclass
class FilterParams:
    func: Union[Callable, Coroutine]
    args: Tuple
    kwargs: Dict


@dataclass
class WaitNext:
    waiter: Union[Callable, Coroutine]
    filters: List[FilterParams]


def _check_sig(func, *args, **kwargs):
    try:
        sig = signature(func)
        sig.bind(*args, **kwargs)
        return True
    except TypeError:
        return False


def make_filter(filter_func: Callable[['Context'], bool]):
    """Make filter"""

    @wraps(filter_func)
    def outer(*args, **kwargs):
        def inner(handler_func: Callable):
            # Checking if function is registered in dispatcher or as waiter.
            assert not hasattr(handler_func, HANDLER_ASSIGNED_ATTR), 'Handler already registered!'
            assert not hasattr(handler_func, WAITER_ASSIGNED_ATTR), 'Already registered as waiter!'

            # Checking calling signature for filter_func.
            # This prevents runtime errors when wrong
            # arguments passed to filter.
            # object() means Context, passing to filter at runtime.
            assert _check_sig(filter_func, object(), *args, **kwargs), \
                'Wrong arguments passed to filter `%s`!' % filter_func.__name__

            # Set property to handler function.
            params = getattr(handler_func, FILTERS_ATTR, list())
            assert isinstance(params, list), 'Handler function has wrong filters!'
            params.insert(0, FilterParams(filter_func, args, kwargs))
            setattr(handler_func, FILTERS_ATTR, params)

            return handler_func

        return inner

    return outer


def priority(pri: int):
    def inner(handler_func: Callable[['Context'], None]):
        # Checking if function is registered in dispatcher or as waiter.
        assert not hasattr(handler_func, HANDLER_ASSIGNED_ATTR), 'Handler already registered!'
        assert not hasattr(handler_func, WAITER_ASSIGNED_ATTR), 'Already registered as waiter!'

        # Check if priority already set.
        assert not hasattr(handler_func, PRIORITY_ATTR), 'Priority already set!'

        setattr(handler_func, PRIORITY_ATTR, pri)

        return handler_func

    return inner


def make_waiter(waiter_func: Callable[['Context'], bool]):
    """Make waiter"""

    # Checking if function is registered in dispatcher or as waiter.
    assert not hasattr(waiter_func, HANDLER_ASSIGNED_ATTR), 'Handler already registered!'
    assert not hasattr(waiter_func, WAITER_ASSIGNED_ATTR), 'Already registered as waiter!'

    # Priority can't be used in waiters
    if hasattr(waiter_func, PRIORITY_ATTR):
        raise TypeError('Priority can\'t be used in waiters!')

    filters = getattr(waiter_func, FILTERS_ATTR, list())
    assert isinstance(filters, list), 'Waiter function has wrong filters!'

    setattr(waiter_func, WAITER_ASSIGNED_ATTR, True)

    @wraps(waiter_func)
    def inner() -> WaitNext:
        return WaitNext(waiter_func, filters)

    return inner
