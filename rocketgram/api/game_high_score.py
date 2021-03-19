# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .user import User


@dataclass(frozen=True)
class GameHighScore:
    """\
    Represents GameHighScore object:
    https://core.telegram.org/bots/api#gamehighscore
    """

    position: int
    user: User
    score: int

    @classmethod
    def parse(cls, data: dict) -> Optional['GameHighScore']:
        if data is None:
            return None

        return cls(data['position'], User.parse(data['user']), data.get('score'))
