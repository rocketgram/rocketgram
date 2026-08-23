# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional, List

from .message_entity import MessageEntity
from .poll_option import PollOption
from .poll_type import PollType
from .poll_media import PollMedia


@dataclass(frozen=True)
class Poll:
    """\
    Represents Poll object:
    https://core.telegram.org/bots/api#poll
    """

    id: str
    question: str
    question_entities: Optional[List[MessageEntity]]
    options: List[PollOption]
    total_voter_count: int
    is_closed: bool
    is_anonymous: bool
    type: PollType
    allows_multiple_answers: bool
    explanation: Optional[str]
    explanation_entities: Optional[List[MessageEntity]]
    open_period: Optional[int]
    close_date: Optional[datetime]
    media: Optional[PollMedia]
    explanation_media: Optional[PollMedia]
    members_only: bool
    country_codes: Optional[List[str]]
    allows_revoting: bool
    correct_option_ids: Optional[List[int]]
    description: Optional[str]
    description_entities: Optional[List[MessageEntity]]

    @classmethod
    def parse(cls, data: dict) -> Optional['Poll']:
        if data is None:
            return None

        question_entities = [MessageEntity.parse(d) for d in data['question_entities']] \
            if 'question_entities' in data else None
        options = [PollOption.parse(i) for i in data['options']]
        explanation_entities = [MessageEntity.parse(d) for d in data['explanation_entities']] \
            if 'explanation_entities' in data else None
        close_date = datetime.fromtimestamp(data['close_date'], tz=timezone.utc) if 'close_date' in data else None

        return cls(data['id'], data['question'], question_entities, options, data['total_voter_count'],
                   data['is_closed'],
                   data['is_anonymous'], PollType(data['type']), data['allows_multiple_answers'],
                   data.get('explanation'), explanation_entities,
                   data.get('open_period'), close_date, PollMedia.parse(data.get('media')),
                   PollMedia.parse(data.get('explanation_media')), data['members_only'],
                    data.get('country_codes'), data['allows_revoting'], data.get('correct_option_ids'),
                   data.get('description'),
                   [MessageEntity.parse(d) for d in data['description_entities']]
                   if 'description_entities' in data else None)
