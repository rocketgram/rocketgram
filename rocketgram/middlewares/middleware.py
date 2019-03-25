# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).


import typing

if typing.TYPE_CHECKING:
    from ..bot import Bot
    from ..context import Context
    from ..update import Response
    from ..requests import Request


class Middleware:
    def init(self, bot: 'Bot'):
        raise NotImplementedError

    def shutdown(self, bot: 'Bot'):
        raise NotImplementedError

    def process(self, context: 'Context') -> 'Context':
        raise NotImplementedError

    def process_error(self, context: 'Context', error: Exception):
        raise NotImplementedError

    def before_request(self, bot: 'Bot', request: 'Request') -> 'Request':
        raise NotImplementedError

    def after_request(self, bot: 'Bot', request: 'Request', response: 'Response') -> 'Response':
        raise NotImplementedError

    def request_error(self, bot: 'Bot', request: 'Request', error: Exception):
        raise NotImplementedError


class EmptyMiddleware(Middleware):
    def init(self, bot: 'Bot'):
        pass

    def shutdown(self, bot: 'Bot'):
        pass

    def process(self, context: 'Context') -> 'Context':
        return context

    def process_error(self, context: 'Context', error: Exception):
        pass

    def before_request(self, bot: 'Bot', request: 'Request') -> 'Request':
        return request

    def after_request(self, bot: 'Bot', request: 'Request', response: 'Response') -> 'Response':
        return response

    def request_error(self, bot: 'Bot', request: 'Request', error: Exception):
        pass
