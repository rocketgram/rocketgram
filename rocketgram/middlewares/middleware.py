# Copyright (C) 2015-2019 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


import typing

if typing.TYPE_CHECKING:
    from ..update import Response
    from ..requests import Request


class Middleware:
    def init(self):
        raise NotImplementedError

    def shutdown(self):
        raise NotImplementedError

    def before_process(self):
        raise NotImplementedError

    def after_process(self):
        raise NotImplementedError

    def process_error(self, error: Exception):
        raise NotImplementedError

    def before_request(self, request: 'Request') -> 'Request':
        raise NotImplementedError

    def after_request(self, request: 'Request', response: 'Response') -> 'Response':
        raise NotImplementedError

    def request_error(self, request: 'Request', error: Exception):
        raise NotImplementedError


class EmptyMiddleware(Middleware):
    def init(self):
        pass

    def shutdown(self):
        pass

    def before_process(self):
        pass

    def after_process(self):
        pass

    def process_error(self, error: Exception):
        pass

    def before_request(self, request: 'Request') -> 'Request':
        return request

    def after_request(self, request: 'Request', response: 'Response') -> 'Response':
        return response

    def request_error(self, request: 'Request', error: Exception):
        pass
