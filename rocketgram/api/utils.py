# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from enum import Enum
from typing import Union

from .. import api
from .. import keyboards


class EnumAutoName(Enum):
    """Class for named enums."""

    def _generate_next_value_(self, start, count, last_values):
        return self


ALL_KEYBOARDS = Union['api.InlineKeyboard',
                      'api.ReplyKeyboard',
                      'api.InlineKeyboardMarkup',
                      'api.ReplyKeyboardMarkup',
                      'api.ReplyKeyboardRemove',
                      'force_reply.ForceReply']
INLINE_KEYBOARDS = Union['keyboards.InlineKeyboard', 'api.InlineKeyboardMarkup']
