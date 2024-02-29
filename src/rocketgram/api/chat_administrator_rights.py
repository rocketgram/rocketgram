# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class ChatAdministratorRights:
    """\
    Represents ChatAdministratorRights object:
    https://core.telegram.org/bots/api#chatadministratorrights
    """

    is_anonymous: Optional[bool]
    can_manage_chat: Optional[bool]
    can_delete_messages: Optional[bool]
    can_manage_video_chats: Optional[bool]
    can_restrict_members: Optional[bool]
    can_promote_members: Optional[bool]
    can_change_info: Optional[bool]
    can_invite_users: Optional[bool]
    can_post_stories: Optional[bool]
    can_edit_stories: Optional[bool]
    can_delete_stories: Optional[bool]
    can_post_messages: Optional[bool]
    can_edit_messages: Optional[bool]
    can_pin_messages: Optional[bool]
    can_manage_topics: Optional[bool]

    @classmethod
    def parse(cls, data: dict) -> Optional['ChatAdministratorRights']:
        if data is None:
            return None

        return cls(
            data.get('is_anonymous'),
            data.get('can_manage_chat'),
            data.get('can_delete_messages'),
            data.get('can_manage_video_chats'),
            data.get('can_restrict_members'),
            data.get('can_promote_members'),
            data.get('can_change_info'),
            data.get('can_invite_users'),
            data.get('can_post_stories'),
            data.get('can_edit_stories'),
            data.get('can_delete_stories'),
            data.get('can_post_messages'),
            data.get('can_edit_messages'),
            data.get('can_pin_messages'),
            data.get('can_manage_topics')
        )
