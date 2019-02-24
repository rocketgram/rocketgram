# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).


class TelegramStopRequest(Exception):
    pass


class TelegramConnectionError(Exception):
    pass


class TelegramTimeoutError(Exception):
    pass


class TelegramParseError(Exception):
    pass


class TelegramSendError(Exception):
    def __init__(self, method, request, code, response):
        self.method = method
        self.request = request
        self.code = code
        self.response = response


class UnknownUpdateType(Exception):
    pass
