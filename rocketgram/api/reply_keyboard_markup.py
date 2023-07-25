# Copyright (C) 2015-2023 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, Tuple

from .keyboard_button import KeyboardButton


@dataclass(frozen=True)
class ReplyKeyboardMarkup:
    """\
    Represents ReplyKeyboardMarkup keyboard object:
    https://core.telegram.org/bots/api#replykeyboardmarkup
    """

    keyboard: Tuple[Tuple[KeyboardButton, ...], ...]
    is_persistent: Optional[bool] = None
    resize_keyboard: Optional[bool] = None
    one_time_keyboard: Optional[bool] = None
    input_field_placeholder: Optional[str] = None
    selective: Optional[bool] = None
