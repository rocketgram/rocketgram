# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Dict, Optional

from . import chat
from . import chat_invite_link
from . import chat_member
from . import user


@dataclass(frozen=True)
class ChatMemberUpdated:
    """\
    Represents ChatMemberUpdated object:
    https://core.telegram.org/bots/api#chatmemberupdated

    Differences in field names:
    from -> user
    """

    chat: 'chat.Chat'
    user: 'user.User'
    date: datetime
    old_chat_member: 'chat_member.ChatMember'
    new_chat_member: 'chat_member.ChatMember'
    invite_link: Optional['chat_invite_link.ChatInviteLink']
    via_chat_folder_invite_link: Optional[bool]

    @classmethod
    def parse(cls, data: Optional[Dict]) -> Optional['ChatMemberUpdated']:
        if data is None:
            return None

        return cls(
            chat.Chat.parse(data['chat']),
            user.User.parse(data['from']),
            datetime.fromtimestamp(data['date'], tz=timezone.utc) if 'date' in data else None,
            chat_member.ChatMember.parse(data['old_chat_member']),
            chat_member.ChatMember.parse(data['new_chat_member']),
            chat_invite_link.ChatInviteLink.parse(data.get('invite_link')),
            data.get('via_chat_folder_invite_link')
        )
