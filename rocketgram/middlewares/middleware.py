# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from typing import Awaitable, Union, Optional

from .. import api


class Middleware:
    def init(self) -> Optional[Awaitable]:
        raise NotImplementedError

    def shutdown(self) -> Optional[Awaitable]:
        raise NotImplementedError

    def before_process(self) -> Optional[Awaitable]:
        raise NotImplementedError

    def after_process(self) -> Optional[Awaitable]:
        raise NotImplementedError

    def process_error(self, error: Exception) -> Optional[Awaitable]:
        raise NotImplementedError

    def before_request(self, request: 'api.Request') -> Union['api.Response', Awaitable['api.Request']]:
        raise NotImplementedError

    def after_request(self, request: 'api.Request', response: 'api.Response') -> \
            Union['api.Response', Awaitable['api.Response']]:
        raise NotImplementedError

    def request_error(self, request: 'api.Request', error: Exception) -> Optional[Awaitable]:
        raise NotImplementedError


class EmptyMiddleware(Middleware):
    def init(self) -> Optional[Awaitable]:
        pass

    def shutdown(self) -> Optional[Awaitable]:
        pass

    def before_process(self) -> Optional[Awaitable]:
        pass

    def after_process(self) -> Optional[Awaitable]:
        pass

    def process_error(self, error: Exception) -> Optional[Awaitable]:
        pass

    def before_request(self, request: 'api.Request') -> Union['api.Request', Awaitable['api.Request']]:
        return request

    def after_request(self, request: 'api.Request', response: 'api.Response') -> \
            Union['api.Response', Awaitable['api.Response']]:
        return response

    def request_error(self, request: 'api.Request', error: Exception) -> Optional[Awaitable]:
        pass
