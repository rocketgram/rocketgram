# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import replace

from .middleware import EmptyMiddleware
from ..api import Request


class DefaultValuesMiddleware(EmptyMiddleware):
    __slots__ = ('__defaults',)

    def __init__(self, **defaults):
        self.__defaults = defaults.copy()

    @property
    def defaults(self):
        return self.__defaults.copy()

    def before_request(self, request: Request) -> Request:
        replaces = dict()

        for k, v in self.__defaults.items():
            if hasattr(request, k) and getattr(request, k) is None:
                replaces[k] = v

        if len(replaces):
            return replace(request, **replaces)  # noqa

        return request
