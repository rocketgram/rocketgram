# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional, List

from .message_entity import MessageEntity
from .poll_option import PollOption
from .poll_type import PollType


@dataclass(frozen=True)
class Poll:
    """\
    Represents Poll object:
    https://core.telegram.org/bots/api#poll
    """

    id: str
    question: str
    options: List[PollOption]
    total_voter_count: int
    is_closed: bool
    is_anonymous: bool
    type: PollType
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
        explanation_entities = [MessageEntity.parse(d) for d in data['explanation_entities']] \
            if 'explanation_entities' in data else None
        close_date = datetime.fromtimestamp(data['close_date'], tz=timezone.utc) if 'close_date' in data else None

        return cls(data['id'], data['question'], options, data['total_voter_count'], data['is_closed'],
                   data['is_anonymous'], PollType(data['type']), data['allows_multiple_answers'],
                   data.get('correct_option_id'), data.get('explanation'), explanation_entities,
                   data.get('open_period'), close_date)
