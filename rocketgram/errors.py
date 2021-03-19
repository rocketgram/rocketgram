# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).

from typing import ClassVar

from . import api


class RocketgramError(Exception):
    """Base exception for all RocketgramErrors"""
    pass


class RocketgramNetworkError(RocketgramError):
    """\
    Exception indicates error from connector.
    """

    def __init__(self, exception: Exception):
        self.exception = exception

    def __str__(self):
        return "Network error: %s: %s" % (type(self.exception).__name__, self.exception)


class RocketgramParseError(RocketgramError):
    """\
    Exception indicates error from json-parser.
    """

    def __init__(self, exception: Exception):
        self.exception = exception

    def __str__(self):
        return "Parser error: %s: %s" % (type(self.exception).__name__, self.exception)


class RocketgramRequestError(RocketgramError):
    """\
    Base exception for all request-related errors.
    """

    _exceptions = {}
    error_code = None

    def __init__(self, request: 'api.Request', response: 'api.Response'):
        self.request = request
        self.response = response

    def __str__(self):
        return self.response.description

    @classmethod
    def register_exception(cls, exception: ClassVar['RocketgramRequestError']) -> ClassVar['RocketgramRequestError']:
        assert exception.error_code is not None
        assert exception.error_code not in cls._exceptions
        assert issubclass(exception, RocketgramRequestError)

        cls._exceptions[exception.error_code] = exception
        return exception

    @classmethod
    def get_exception(cls, request: 'api.Request', response: 'api.Response') -> 'RocketgramRequestError':
        exception = cls._exceptions.get(response.error_code, RocketgramRequestError)

        return exception(request, response)


@RocketgramRequestError.register_exception
class RocketgramRequest400Error(RocketgramRequestError):
    """\
    Exception indicates errors with code 400.
    """

    error_code = 400


@RocketgramRequestError.register_exception
class RocketgramRequest401Error(RocketgramRequestError):
    """\
    Exception indicates errors with code 401.
    """

    error_code = 401


@RocketgramRequestError.register_exception
class RocketgramRequest429Error(RocketgramRequestError):
    """\
    Exception indicates errors with code 429.
    """

    error_code = 429


class RocketgramStopRequest(RocketgramError):
    """\
    A special exception that can be raised to abort request processing.
    Should never be intercepted in user code.
    """
