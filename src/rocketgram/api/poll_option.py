# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List

from .message_entity import MessageEntity


@dataclass(frozen=True)
class PollOption:
    """\
    Represents PollOption object:
    https://core.telegram.org/bots/api#polloption
    """

    text: str
    text_entities: Optional[List[MessageEntity]]
    voter_count: int

    @classmethod
    def parse(cls, data: dict) -> Optional['PollOption']:
        if data is None:
            return None

        return cls(
            data['text'],
            [MessageEntity.parse(e) for e in data['text_entities']] if 'text_entities' in data else None,
            data['voter_count']
        )
