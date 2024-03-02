# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from enum import Enum
from typing import Union

from .. import api
from .. import keyboards  # noqa
from ..context import context


class EnumAutoName(Enum):
    """Class for named enums."""

    def _generate_next_value_(self, start, count, last_values):
        return self


class BoolResultMixin:
    """Mixin for request classes that returns bool"""

    @staticmethod
    def parse_result(data) -> bool:
        assert isinstance(data, bool), "Should be bool."
        return data

    async def send(self: 'api.Request') -> bool:
        res = await context.bot.send(self)
        return res.result


class IntResultMixin:
    """Mixin for request classes that returns int"""

    @staticmethod
    def parse_result(data) -> int:  # noqa
        assert isinstance(data, int), "Should be int."
        return data

    async def send(self: 'api.Request') -> int:
        res = await context.bot.send(self)
        return res.result


class StrResultMixin:
    """Mixin for request classes that returns str"""

    @staticmethod
    def parse_result(data) -> str:  # noqa
        assert isinstance(data, str), "Should be str."
        return data

    async def send(self: 'api.Request') -> str:
        res = await context.bot.send(self)
        return res.result


class MessageResultMixin:
    """Mixin for request classes that returns Message"""

    @staticmethod
    def parse_result(data) -> 'api.Message':  # noqa
        assert isinstance(data, dict), "Should be dict."
        return api.Message.parse(data)

    async def send(self: 'api.Request') -> 'api.Message':
        res = await context.bot.send(self)
        return res.result


class MessageOrBoolResultMixin:
    """Mixin for request classes that returns Message or bool"""

    @staticmethod
    def parse_result(data) -> Union['api.Message', bool]:  # noqa
        assert isinstance(data, (dict, bool)), "Should be dict or bool."
        return data if isinstance(data, bool) else api.Message.parse(data)

    async def send(self: 'api.Request') -> Union['api.Message', bool]:
        res = await context.bot.send(self)
        return res.result


class FileResultMixin:
    """Mixin for request classes that returns File"""

    @staticmethod
    def parse_result(data) -> 'api.File':
        assert isinstance(data, dict), "Should be dict."
        return api.File.parse(data)

    async def send(self: 'api.Request') -> 'api.File':
        res = await context.bot.send(self)
        return res.result


class ChatInviteLinkResultMixin:
    """Mixin for request classes that returns ChatInviteLink"""

    @staticmethod
    def parse_result(data) -> 'api.ChatInviteLink':
        assert isinstance(data, dict), "Should be dict."
        return api.ChatInviteLink.parse(data)

    async def send(self: 'api.Request') -> 'api.ChatInviteLink':
        res = await context.bot.send(self)
        return res.result


AnyInlineKeyboard = Union['keyboards.InlineKeyboard', 'api.InlineKeyboardMarkup']

AnyKeyboard = Union[
    AnyInlineKeyboard,
    'keyboards.ReplyKeyboard',
    'api.ReplyKeyboardMarkup',
    'api.ReplyKeyboardRemove',
    'api.ForceReply'
]
