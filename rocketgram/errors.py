# Copyright (C) 2015-2019 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .requests import Request
    from .update import Response


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

    def __init__(self, request: 'Request', response: 'Response'):
        self.request = request
        self.response = response

    def __str__(self):
        return self.response.description


class RocketgramRequest400Error(RocketgramRequestError):
    """\
    Exception indicates errors with code 400.
    """


class RocketgramRequest401Error(RocketgramRequestError):
    """\
    Exception indicates errors with code 401.
    """


class RocketgramRequest429Error(RocketgramRequestError):
    """\
    Exception indicates errors with code 429.
    """


class RocketgramStopRequest(RocketgramError):
    """\
    A special exception that can be raised to abort request processing.
    Should never be intercepted in user code.
    """
