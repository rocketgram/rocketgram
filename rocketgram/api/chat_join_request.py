# Copyright (C) 2015-2022 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Optional

from .chat import Chat
from .chat_invite_link import ChatInviteLink
from .user import User


@dataclass(frozen=True)
class ChatJoinRequest:
    """\
    Represents ChatJoinRequest object:
    https://core.telegram.org/bots/api#chatjoinrequest

    Differences in field names:
    from -> user
    """

    chat: Chat
    user: User
    date: datetime
    bio: Optional[str]
    invite_link: Optional[ChatInviteLink]

    @classmethod
    def parse(cls, data: Optional[Dict]) -> Optional['ChatJoinRequest']:
        if data is None:
            return None

        return cls(Chat.parse(data['chat']), User.parse(data['from']), datetime.utcfromtimestamp(data['date']),
                   data.get('bio'), ChatInviteLink.parse(data.get('invite_link')))
