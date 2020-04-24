# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

from .message_entity import MessageEntity
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
    explanation: Optional[str]
    explanation_entities: Optional[List[MessageEntity]]
    open_period: Optional[int]
    close_date: Optional[datetime]

    @classmethod
    def parse(cls, data: dict) -> Optional['Poll']:
        if data is None:
            return None

        options = [PollOption.parse(i) for i in data['options']]
        explanation_entities = [MessageEntity.parse(d) for d in
                                data.get('explanation_entities')] if 'explanation_entities' in data else None
        close_date = datetime.utcfromtimestamp(data['close_date']) if 'close_date' in data else None

        return cls(data['id'], data['question'], options, data['total_voter_count'], data['is_closed'],
                   data['is_anonymous'], PollType(data['type']), data['allows_multiple_answers'],
                   data.get('correct_option_id'), data.get('explanation'), explanation_entities,
                   data.get('open_period'), close_date)
