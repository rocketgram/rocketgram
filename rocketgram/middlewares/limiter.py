# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).


import typing
from time import monotonic

if typing.TYPE_CHECKING:
    from ..context import Context

from .middleware import EmptyMiddleware
from ..errors import RocketgramStopRequest


class LimiterMiddleware(EmptyMiddleware):
    """\
    This middleware pass no more than `quantity` messages per `period` seconds.
    """

    __slots__ = ('__quantity', '__period', '__values')

    def __init__(self, quantity: int, period: float):
        self.__quantity = quantity
        self.__period = period
        self.__values = list()

    def process(self, context: 'Context') -> 'Context':
        current = monotonic()
        d = current - self.__period

        self.__values = [v for v in self.__values if v > d]

        if len(self.__values) >= self.__quantity:
            raise RocketgramStopRequest(f'Update `{context.update.update_id}` was dropped due to '
                                        f'rate exceed `{self.__quantity}` msg per `{self.__period} secs.`')

        self.__values.append(current)

        return context
