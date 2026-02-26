# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class UserRating:
    """\
    Represents UserRating object:
    https://core.telegram.org/bots/api#userrating
    """

    level: int
    rating: int
    current_level_rating: int
    next_level_rating: Optional[int]

    @classmethod
    def parse(cls, data: dict) -> Optional['UserRating']:
        if data is None:
            return None

        return cls(
            data['level'],
            data['rating'],
            data['current_level_rating'],
            data.get('next_level_rating'),
        )
