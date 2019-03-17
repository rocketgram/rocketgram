from dataclasses import dataclass
from functools import wraps
from inspect import signature
from typing import Callable, Tuple, Dict, TYPE_CHECKING

FILTERS_ATTR = 'rocketgram_dispatcher_filters'
PRIORITY_ATTR = 'rocketgram_dispatcher_handler_priority'
HANDLER_ASSIGNED_ATTR = 'rocketgram_dispatcher_handler_assigned'
WAITER_ASSIGNED_ATTR = 'rocketgram_dispatcher_waiter_assigned'

if TYPE_CHECKING:
    from ...context import Context


@dataclass
class FilterParams:
    func: Callable
    args: Tuple
    kwargs: Dict


# @dataclass
# class FilterOr:
#     pass


def make_filter(filter_func: Callable[['Context'], bool]):
    """Make filter"""

    @wraps(filter_func)
    def outer(*args, **kwargs):
        def inner(handler_func: Callable):
            # Checking if function is registered in dispatcher or as waiter.
            if hasattr(handler_func, HANDLER_ASSIGNED_ATTR):
                raise TypeError('Handler already registered!')
            if hasattr(handler_func, WAITER_ASSIGNED_ATTR):
                raise TypeError('Already registered as waiter!')

            # Checking calling signature for filter_func.
            # This prevents runtime errors when wrong
            # arguments passed to filter.
            try:
                sig = signature(filter_func)
                # object() means Context, passing to filter at runtime.
                sig.bind(object(), *args, **kwargs)
            except TypeError as e:
                es = 'Wrong arguments passed to filter `%s`: %s' % (filter_func.__name__, e)
                raise TypeError(es) from None

            # Set property to handler function.
            params = getattr(handler_func, FILTERS_ATTR, list())
            params.insert(0, FilterParams(filter_func, args, kwargs))
            setattr(handler_func, FILTERS_ATTR, params)

            return handler_func

        return inner

    return outer


# def filter_or(handler_func: Callable[['Context', ...], None]):
#
#     # Checking if function is registered in dispatcher or as waiter.
#     if hasattr(handler_func, HANDLER_ASSIGNED_ATTR):
#         raise TypeError('Handler already registered!')
#     if hasattr(handler_func, WAITER_ASSIGNED_ATTR):
#         raise TypeError('Already registered as waiter!')
#
#     params = getattr(handler_func, FILTERS_ATTR, list())
#     params.insert(0, FilterOr())
#     setattr(handler_func, FILTERS_ATTR, params)
#
#     return handler_func


def priority(pri: int):
    def inner(handler_func: Callable[['Context'], None]):

        # Checking if function is registered in dispatcher or as waiter.
        if hasattr(handler_func, HANDLER_ASSIGNED_ATTR):
            raise TypeError('Handler already registered!')
        if hasattr(handler_func, WAITER_ASSIGNED_ATTR):
            raise TypeError('Already registered as waiter!')

        # Checking is handler is registered in dispatcher.
        if hasattr(handler_func, PRIORITY_ATTR):
            raise TypeError('Priority for handler already set!')

        setattr(handler_func, PRIORITY_ATTR, pri)

        return handler_func

    return inner


def waiter(waiter_func: Callable[['Context'], None]):
    # Checking if function is registered in dispatcher or as waiter.
    if hasattr(waiter_func, HANDLER_ASSIGNED_ATTR):
        raise TypeError('Already registered as handler!')
    if hasattr(waiter_func, WAITER_ASSIGNED_ATTR):
        raise TypeError('Already registered as waiter!')

    # Priority can't be used in waiters
    if hasattr(waiter_func, PRIORITY_ATTR):
        raise TypeError('Priority can\'t be used in waiters!')

    # Checking calling signature for waiter_func.
    try:
        sig = signature(waiter_func)
        # object() means Context, passing to handler at runtime.
        sig.bind(object())
    except TypeError as e:
        es = 'Waiter `%s` must take exactly one argument `ctx: Context`!' % waiter_func.__name__
        raise TypeError(es) from None

    setattr(waiter_func, WAITER_ASSIGNED_ATTR, True)
    return waiter_func
