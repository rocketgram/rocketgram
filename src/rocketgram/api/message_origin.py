# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Dict, Optional

from . import chat
from . import user
from .message_origin_type import MessageOriginType


@dataclass(frozen=True)
class MessageOrigin:
    """\
    Represents MessageOrigin, MessageOriginUser, MessageOriginHiddenUser,
    MessageOriginChat, MessageOriginChannel objects:
    https://core.telegram.org/bots/api#messageorigin
    """

    type: MessageOriginType
    date: datetime
    sender_user: Optional['user.User']
    sender_user_name: Optional[str]
    sender_chat: Optional['chat.Chat']
    chat: Optional['chat.Chat']
    message_id: Optional[int]
    author_signature: Optional[str]

    @classmethod
    def parse(cls, data: Optional[Dict]) -> Optional['MessageOrigin']:
        if data is None:
            return None

        try:
            message_origin_type = MessageOriginType(data['type'])
        except ValueError:
            message_origin_type = MessageOriginType.unknown

        return cls(
            message_origin_type,
            datetime.fromtimestamp(data['date'], tz=timezone.utc),
            user.User.parse(data.get('sender_user')),
            data.get('sender_user_name'),
            chat.Chat.parse(data.get('sender_chat')),
            chat.Chat.parse(data.get('chat')),
            data.get('message_id'),
            data.get('author_signature'),
        )
