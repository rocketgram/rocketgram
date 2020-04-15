# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from enum import Enum
from typing import Union, TypeVar

from . import force_reply, inline_keyboard_markup
from .. import keyboards


class EnumAutoName(Enum):
    """Class for named enums."""

    def _generate_next_value_(self, start, count, last_values):
        return self


ALL_KEYBOARDS = Union['keyboards.InlineKeyboard',
                      'keyboards.ReplyKeyboard',
                      'keyboards.InlineKeyboardMarkup',
                      'keyboards.ReplyKeyboardMarkup',
                      'keyboards.ReplyKeyboardRemove',
                      'force_reply.ForceReply']
INLINE_KEYBOARDS = Union['InlineKeyboard', 'inline_keyboard_markup.InlineKeyboardMarkup']
