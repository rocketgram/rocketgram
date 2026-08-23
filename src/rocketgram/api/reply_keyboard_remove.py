# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class ReplyKeyboardRemove:
    """\
    Represents ReplyKeyboardRemove keyboard object:
    https://core.telegram.org/bots/api#replykeyboardremove
    """

    selective: Optional[bool] = None
    remove_keyboard: bool = True
