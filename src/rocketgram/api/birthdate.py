# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Birthdate:
    """\
    Represents Birthdate object:
    https://core.telegram.org/bots/api#birthdate
    """

    day: int
    month: int
    year: Optional[int]

    @classmethod
    def parse(cls, data: dict) -> Optional['Birthdate']:
        if data is None:
            return None

        return cls(
            data['day'],
            data['month'],
            data.get('year'),
        )
