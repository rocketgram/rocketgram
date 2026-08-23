# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional, List

from . import chat
from .message_entity import MessageEntity
from .poll_media import PollMedia
from .user import User


@dataclass(frozen=True)
class PollOption:
    """\
    Represents PollOption object:
    https://core.telegram.org/bots/api#polloption
    """

    text: str
    text_entities: Optional[List[MessageEntity]]
    voter_count: int
    media: Optional[PollMedia]
    persistent_id: str
    added_by_user: Optional[User]
    added_by_chat: Optional['chat.Chat']
    addition_date: Optional[datetime]

    @classmethod
    def parse(cls, data: dict) -> Optional['PollOption']:
        if data is None:
            return None

        return cls(
            data['text'],
            [MessageEntity.parse(e) for e in data['text_entities']] if 'text_entities' in data else None,
            data['voter_count'],
            PollMedia.parse(data.get('media')),
            data['persistent_id'],
            User.parse(data.get('added_by_user')),
            chat.Chat.parse(data.get('added_by_chat')),
            datetime.fromtimestamp(data['addition_date'], tz=timezone.utc) if 'addition_date' in data else None,
        )
