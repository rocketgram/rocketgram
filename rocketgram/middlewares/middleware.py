# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from typing import TYPE_CHECKING, Awaitable, Union, Optional

if TYPE_CHECKING:
    from ..update import Response
    from ..requests import Request


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

    def before_request(self, request: 'Request') -> Union['Response', Awaitable['Request']]:
        raise NotImplementedError

    def after_request(self, request: 'Request', response: 'Response') -> Union['Response', Awaitable['Response']]:
        raise NotImplementedError

    def request_error(self, request: 'Request', error: Exception) -> Optional[Awaitable]:
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

    def before_request(self, request: 'Request') -> Union['Response', Awaitable['Request']]:
        return request

    def after_request(self, request: 'Request', response: 'Response') -> Union['Response', Awaitable['Response']]:
        return response

    def request_error(self, request: 'Request', error: Exception) -> Optional[Awaitable]:
        pass
