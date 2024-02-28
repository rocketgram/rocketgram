# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Dict, Optional, List

from . import message
from .chat_location import ChatLocation
from .chat_permissions import ChatPermissions
from .chat_photo import ChatPhoto
from .chat_type import ChatType
from .reaction_type import ReactionType


@dataclass(frozen=True)
class Chat:
    """\
    Represents Chat object:
    https://core.telegram.org/bots/api#chat
    """

    id: int
    type: ChatType
    title: Optional[str]
    username: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    is_forum: Optional[bool]
    photo: Optional[ChatPhoto]
    active_usernames: Optional[List[str]]
    available_reactions: Optional[List[ReactionType]]
    accent_color_id: Optional[int]
    background_custom_emoji_id: Optional[str]
    profile_accent_color_id: Optional[int]
    profile_background_custom_emoji_id: Optional[str]
    emoji_status_custom_emoji_id: Optional[str]
    emoji_status_expiration_date: Optional[datetime]
    bio: Optional[str]
    has_private_forwards: Optional[bool]
    has_restricted_voice_and_video_messages: Optional[bool]
    join_to_send_messages: Optional[bool]
    join_by_request: Optional[bool]
    description: Optional[str]
    invite_link: Optional[str]
    pinned_message: Optional['message.Message']
    permissions: Optional[ChatPermissions]
    slow_mode_delay: Optional[int]
    unrestrict_boost_count: Optional[int]
    message_auto_delete_time: Optional[int]
    has_aggressive_anti_spam_enabled: Optional[bool]
    has_hidden_members: Optional[bool]
    has_protected_content: Optional[bool]
    has_visible_history: Optional[bool]
    sticker_set_name: Optional[str]
    can_set_sticker_set: Optional[bool]
    custom_emoji_sticker_set_name: Optional[str]
    linked_chat_id: Optional[int]
    location: Optional[ChatLocation]

    @classmethod
    def parse(cls, data: Optional[Dict]) -> Optional['Chat']:
        if data is None:
            return None

        try:
            chat_type = ChatType(data['type'])
        except ValueError:
            chat_type = ChatType.unknown
        return cls(
            data['id'],
            chat_type,
            data.get('title'),
            data.get('username'),
            data.get('first_name'),
            data.get('last_name'),
            data.get('is_forum'),
            ChatPhoto.parse(data.get('photo')),
            data['active_usernames'] if 'active_usernames' in data else None,
            [ReactionType.parse(r) for r in data['available_reactions']] if 'available_reactions' in data else None,
            data.get('accent_color_id'),
            data.get('background_custom_emoji_id'),
            data.get('profile_accent_color_id'),
            data.get('profile_background_custom_emoji_id'),
            data.get('emoji_status_custom_emoji_id'),
            datetime.fromtimestamp(data['emoji_status_expiration_date'],
                                   tz=timezone.utc) if 'emoji_status_expiration_date' in data else None,
            data.get('bio'),
            data.get('has_private_forwards'),
            data.get('has_restricted_voice_and_video_messages'),
            data.get('join_to_send_messages'),
            data.get('join_by_request'),
            data.get('description'),
            data.get('invite_link'),
            message.Message.parse(data.get('pinned_message')),
            ChatPermissions.parse(data.get('permissions')),
            data.get('slow_mode_delay'),
            data.get('unrestrict_boost_count'),
            data.get('message_auto_delete_time'),
            data.get('has_aggressive_anti_spam_enabled'),
            data.get('has_hidden_members'),
            data.get('has_protected_content'),
            data.get('has_visible_history'),
            data.get('sticker_set_name'),
            data.get('can_set_sticker_set'),
            data.get('custom_emoji_sticker_set_name'),
            data.get('linked_chat_id'),
            ChatLocation.parse(data.get('location'))
        )
