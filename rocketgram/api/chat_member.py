# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional

from .chat_member_status_type import ChatMemberStatusType
from .user import User


@dataclass(frozen=True)
class ChatMember:
    """\
    Represents ChatMember, ChatMemberOwner, ChatMemberAdministrator, ChatMemberMember,
    ChatMemberRestricted, ChatMemberLeft, and ChatMemberBanned objects:
    https://core.telegram.org/bots/api#chatmember
    https://core.telegram.org/bots/api#chatmemberowner
    https://core.telegram.org/bots/api#chatmemberadministrator
    https://core.telegram.org/bots/api#chatmembermember
    https://core.telegram.org/bots/api#chatmemberrestricted
    https://core.telegram.org/bots/api#chatmemberleft
    https://core.telegram.org/bots/api#chatmemberbanned
    """

    user: User
    status: ChatMemberStatusType
    custom_title: Optional[str]
    is_anonymous: Optional[bool]
    until_date: Optional[datetime]
    can_be_edited: Optional[bool]
    can_manage_chat: Optional[bool]
    can_change_info: Optional[bool]
    can_post_messages: Optional[bool]
    can_edit_messages: Optional[bool]
    can_delete_messages: Optional[bool]
    can_manage_video_chats: Optional[bool]
    can_invite_users: Optional[bool]
    can_post_stories: Optional[bool]
    can_edit_stories: Optional[bool]
    can_delete_stories: Optional[bool]
    can_restrict_members: Optional[bool]
    can_pin_messages: Optional[bool]
    can_manage_topics: Optional[bool]
    can_promote_members: Optional[bool]
    is_member: Optional[bool]
    can_send_messages: Optional[bool]
    can_send_audios: Optional[bool]
    can_send_documents: Optional[bool]
    can_send_photos: Optional[bool]
    can_send_videos: Optional[bool]
    can_send_video_notes: Optional[bool]
    can_send_voice_notes: Optional[bool]
    can_send_polls: Optional[bool]
    can_send_other_messages: Optional[bool]
    can_add_web_page_previews: Optional[bool]

    @classmethod
    def parse(cls, data: dict) -> Optional['ChatMember']:
        if data is None:
            return None

        return cls(
            User.parse(data['user']),
            ChatMemberStatusType(data['status']),
            data.get('custom_title'),
            data.get('is_anonymous'),
            datetime.fromtimestamp(data['until_date'], tz=timezone.utc) if 'until_date' in data else None,
            data.get('can_be_edited'),
            data.get('can_manage_chat'),
            data.get('can_change_info'),
            data.get('can_post_messages'),
            data.get('can_edit_messages'),
            data.get('can_delete_messages'),
            data.get('can_manage_video_chats'),
            data.get('can_invite_users'),
            data.get('can_post_stories'),
            data.get('can_edit_stories'),
            data.get('can_delete_stories'),
            data.get('can_restrict_members'),
            data.get('can_pin_messages'),
            data.get('can_manage_topics'),
            data.get('can_promote_members'),
            data.get('is_member'),
            data.get('can_send_messages'),
            data.get('can_send_audios'),
            data.get('can_send_documents'),
            data.get('can_send_photos'),
            data.get('can_send_videos'),
            data.get('can_send_video_notes'),
            data.get('can_send_voice_notes'),
            data.get('can_send_polls'),
            data.get('can_send_other_messages'),
            data.get('can_add_web_page_previews'),
        )
