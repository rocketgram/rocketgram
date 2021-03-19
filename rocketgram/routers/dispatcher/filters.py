# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from functools import wraps
from inspect import signature
from typing import Union, Callable, Coroutine, Tuple, Dict

FILTERS_ATTR = 'rocketgram_dispatcher_filters'
PRIORITY_ATTR = 'rocketgram_dispatcher_handler_priority'
HANDLER_ASSIGNED_ATTR = 'rocketgram_dispatcher_handler_assigned'
WAITER_ASSIGNED_ATTR = 'rocketgram_dispatcher_waiter_assigned'


@dataclass(frozen=True)
class FilterParams:
    func: Union[Callable, Coroutine]
    args: Tuple
    kwargs: Dict


def _check_sig(func, *args, **kwargs) -> bool:
    try:
        sig = signature(func)
        sig.bind(*args, **kwargs)
        return True
    except TypeError:
        return False


def make_filter(filter_func: Callable[..., bool]) -> Callable:
    """Makes filter"""

    @wraps(filter_func)
    def outer(*args, **kwargs) -> Callable:
        def inner(handler_func: Callable[..., None]) -> Callable:
            # Checking if function is registered in dispatcher or as waiter.
            assert not hasattr(handler_func, HANDLER_ASSIGNED_ATTR), 'Handler already registered!'
            assert not hasattr(handler_func, WAITER_ASSIGNED_ATTR), 'Already registered as waiter!'

            # Checking calling signature for filter_func.
            # This prevents runtime errors when wrong
            # arguments passed to filter.
            assert _check_sig(filter_func, *args, **kwargs), \
                f'Wrong arguments passed to filter `{filter_func.__name__}`!'

            # Set property to handler function.
            params = getattr(handler_func, FILTERS_ATTR, list())
            assert isinstance(params, list), 'Handler function has wrong filters!'
            params.insert(0, FilterParams(filter_func, args, kwargs))
            setattr(handler_func, FILTERS_ATTR, params)

            return handler_func

        return inner

    return outer


def priority(pri: int) -> Callable:
    def inner(handler_func: Callable[..., None]) -> Callable:
        # Checking if function is registered in dispatcher or as waiter.
        assert not hasattr(handler_func, HANDLER_ASSIGNED_ATTR), 'Handler already registered!'
        assert not hasattr(handler_func, WAITER_ASSIGNED_ATTR), 'Already registered as waiter!'

        # Check if priority already set.
        assert not hasattr(handler_func, PRIORITY_ATTR), 'Priority already set!'

        setattr(handler_func, PRIORITY_ATTR, pri)

        return handler_func

    return inner
