# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Dice:
    """\
    Represents Dice object:
    https://core.telegram.org/bots/api#dice
    """

    emoji: str
    value: int

    @classmethod
    def parse(cls, data: dict) -> Optional['Dice']:
        if data is None:
            return None

        return cls(data['emoji'], data['value'])
