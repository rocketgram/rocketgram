# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import List, Optional

from .poll_option import PollOption
from .poll_type import PollType


@dataclass(frozen=True)
class Poll:
    """\
    Represents Poll object:
    https://core.telegram.org/bots/api#poll

    Differences in field names:
    id -> pool_id
    type -> poll_type

    """

    pool_id: str
    question: str
    options: List[PollOption]
    total_voter_count: int
    is_closed: bool
    is_anonymous: bool
    poll_type: PollType
    allows_multiple_answers: bool
    correct_option_id: Optional[int]

    @classmethod
    def parse(cls, data: dict) -> Optional['Poll']:
        if data is None:
            return None

        options = [PollOption.parse(i) for i in data['options']]

        return cls(data['id'], data['question'], options, data['total_voter_count'], data['is_closed'],
                   data['is_anonymous'], PollType(data['poll_type']), data['allows_multiple_answers'],
                   data['correct_option_id'])
