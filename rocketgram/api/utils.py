# Copyright (C) 2015-2021 by Vd.
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

    def parse_result(self, data) -> bool:  # noqa
        assert isinstance(data, bool), "Should be bool."
        return data

    async def send(self) -> bool:
        res = await context.bot.send(self)
        return res.result


class IntResultMixin:
    """Mixin for request classes that returns int"""

    def parse_result(self, data) -> int:  # noqa
        assert isinstance(data, int), "Should be int."
        return data

    async def send(self) -> int:
        res = await context.bot.send(self)
        return res.result


class StrResultMixin:
    """Mixin for request classes that returns str"""

    def parse_result(self, data) -> str:  # noqa
        assert isinstance(data, str), "Should be str."
        return data

    async def send(self) -> str:
        res = await context.bot.send(self)
        return res.result


class MessageResultMixin:
    """Mixin for request classes that returns Message"""

    def parse_result(self, data) -> 'api.Message':  # noqa
        assert isinstance(data, dict), "Should be dict."
        return api.Message.parse(data)

    async def send(self) -> 'api.Message':
        res = await context.bot.send(self)
        return res.result


class MessageOrBoolResultMixin:
    """Mixin for request classes that returns Message or bool"""

    def parse_result(self, data) -> Union['api.Message', bool]:  # noqa
        assert isinstance(data, (dict, bool)), "Should be dict or bool."
        return data if isinstance(data, bool) else api.Message.parse(data)

    async def send(self) -> Union['api.Message', bool]:
        res = await context.bot.send(self)
        return res.result


class FileResultMixin:
    """Mixin for request classes that returns File"""

    def parse_result(self, data) -> 'api.File':  # noqa
        assert isinstance(data, dict), "Should be dict."
        return api.File.parse(data)

    async def send(self) -> 'api.File':
        res = await context.bot.send(self)
        return res.result


class ChatInviteLinkResultMixin:
    """Mixin for request classes that returns ChatInviteLink"""

    def parse_result(self, data) -> 'api.ChatInviteLink':  # noqa
        assert isinstance(data, dict), "Should be dict."
        return api.ChatInviteLink.parse(data)

    async def send(self) -> 'api.ChatInviteLink':
        res = await context.bot.send(self)
        return res.result


ALL_KEYBOARDS = Union['keyboards.InlineKeyboard',
                      'keyboards.ReplyKeyboard',
                      'api.InlineKeyboardMarkup',
                      'api.ReplyKeyboardMarkup',
                      'api.ReplyKeyboardRemove',
                      'api.ForceReply']
INLINE_KEYBOARDS = Union['keyboards.InlineKeyboard', 'api.InlineKeyboardMarkup']
