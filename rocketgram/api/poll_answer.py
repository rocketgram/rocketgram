# Copyright (C) 2015-2023 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, Tuple

from .user import User


@dataclass(frozen=True)
class PollAnswer:
    """\
    Represents PollAnswer object:
    https://core.telegram.org/bots/api#pollanswer

    """

    poll_id: str
    user: User
    option_ids: Tuple[int, ...]

    @classmethod
    def parse(cls, data: dict) -> Optional['PollAnswer']:
        if data is None:
            return None

        return cls(data['poll_id'], User.parse(data['user']), tuple(data['option_ids']))
