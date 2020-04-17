# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from enum import Enum
from typing import Union

from .. import api


class EnumAutoName(Enum):
    """Class for named enums."""

    def _generate_next_value_(self, start, count, last_values):
        return self


class BoolResultMixin:
    """Mixin for request classes that returns bool"""

    def parse_result(self, data) -> bool:  # noqa
        assert isinstance(data, bool), "Should be bool."
        return data

    async def send2(self) -> bool:
        res = await self._send()  # noqa
        return res.result


class IntResultMixin:
    """Mixin for request classes that returns int"""

    def parse_result(self, data) -> int:  # noqa
        assert isinstance(data, int), "Should be int."
        return data

    async def send2(self) -> int:
        res = await self._send()  # noqa
        return res.result


class StrResultMixin:
    """Mixin for request classes that returns str"""

    def parse_result(self, data) -> str:  # noqa
        assert isinstance(data, str), "Should be str."
        return data

    async def send2(self) -> str:
        res = await self._send()  # noqa
        return res.result


class MessageResultMixin:
    """Mixin for request classes that returns Message"""

    def parse_result(self, data) -> 'api.Message':  # noqa
        assert isinstance(data, dict), "Should be dict."
        return api.Message.parse(data)

    async def send2(self) -> 'api.Message':
        res = await self._send()  # noqa
        return res.result


class MessageOrBoolResultMixin:
    """Mixin for request classes that returns Message or bool"""

    def parse_result(self, data) -> Union['api.Message', bool]:  # noqa
        assert isinstance(data, (dict, bool)), "Should be dict or bool."
        return data if isinstance(data, bool) else api.Message.parse(data)

    async def send2(self) -> Union['api.Message', bool]:
        res = await self._send()  # noqa
        return res.result


class FileResultMixin:
    """Mixin for request classes that returns File"""

    def parse_result(self, data) -> 'api.File':  # noqa
        assert isinstance(data, dict), "Should be dict."
        return api.File.parse(data)

    async def send2(self) -> 'api.File':
        res = await self._send()  # noqa
        return res.result


ALL_KEYBOARDS = Union['api.InlineKeyboard',
                      'api.ReplyKeyboard',
                      'api.InlineKeyboardMarkup',
                      'api.ReplyKeyboardMarkup',
                      'api.ReplyKeyboardRemove',
                      'force_reply.ForceReply']
INLINE_KEYBOARDS = Union['keyboards.InlineKeyboard', 'api.InlineKeyboardMarkup']
