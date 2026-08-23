# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class PreparedKeyboardButton:
    """\
    Represents PreparedKeyboardButton object:
    https://core.telegram.org/bots/api#preparedkeyboardbutton
    """

    id: str

    @classmethod
    def parse(cls, data: dict) -> Optional['PreparedKeyboardButton']:
        if data is None:
            return None
        return cls(data['id'])
