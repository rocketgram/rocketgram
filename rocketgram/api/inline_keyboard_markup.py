# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, Dict, List

from .inline_keyboard_button import InlineKeyboardButton


@dataclass(frozen=True)
class InlineKeyboardMarkup:
    """\
    Represents InlineKeyboardMarkup keyboard object:
    https://core.telegram.org/bots/api#inlinekeyboardmarkup
    """

    inline_keyboard: List[List[InlineKeyboardButton]]

    @classmethod
    def parse(cls, data: Optional[Dict]) -> Optional['InlineKeyboardMarkup']:
        if data is None:
            return None

        return cls([[InlineKeyboardButton.parse(c) for c in r] for r in data['inline_keyboard']])
