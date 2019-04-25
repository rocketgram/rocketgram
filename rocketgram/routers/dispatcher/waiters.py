# Copyright (C) 2015-2019 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from functools import wraps
from typing import List, Union, Callable, Coroutine, Tuple, Dict, TYPE_CHECKING

from .filters import FILTERS_ATTR, PRIORITY_ATTR, HANDLER_ASSIGNED_ATTR, WAITER_ASSIGNED_ATTR
from .filters import _check_sig, FilterParams

if TYPE_CHECKING:
    pass


@dataclass(frozen=True)
class WaitNext:
    waiter: Union[Callable, Coroutine]
    args: Tuple
    kwargs: Dict
    filters: List[FilterParams]


@dataclass(frozen=True)
class DropWaiter:
    pass


def make_waiter(waiter_func: Callable[..., bool]):
    """Make waiter"""

    # Checking if function is registered in dispatcher or as waiter.
    assert not hasattr(waiter_func, HANDLER_ASSIGNED_ATTR), 'Handler already registered!'
    assert not hasattr(waiter_func, WAITER_ASSIGNED_ATTR), 'Already registered as waiter!'

    # Priority can't be used with waiters
    if hasattr(waiter_func, PRIORITY_ATTR):
        raise TypeError('Priority can\'t be used in waiters!')

    filters = getattr(waiter_func, FILTERS_ATTR, list())
    assert isinstance(filters, list), 'Waiter function has wrong filters!'

    setattr(waiter_func, WAITER_ASSIGNED_ATTR, True)

    @wraps(waiter_func)
    def inner(*args, **kwargs) -> WaitNext:
        assert _check_sig(waiter_func, *args, **kwargs), \
            f'Wrong arguments passed to waiter `{waiter_func.__name__}`!'

        return WaitNext(waiter_func, args, kwargs, filters)

    return inner
