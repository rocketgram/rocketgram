# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Dict, Optional, List

from . import chat
from . import message
from .accepted_gift_types import AcceptedGiftTypes
from .audio import Audio
from .birthdate import Birthdate
from .business_intro import BusinessIntro
from .business_location import BusinessLocation
from .business_opening_hours import BusinessOpeningHours
from .chat_location import ChatLocation
from .chat_permissions import ChatPermissions
from .chat_photo import ChatPhoto
from .chat_type import ChatType
from .community import Community
from .reaction_type import ReactionType
from .unique_gift_colors import UniqueGiftColors
from .user_rating import UserRating


@dataclass(frozen=True)
class ChatFullInfo:
    """    Represents ChatFullInfo object:
    https://core.telegram.org/bots/api#chatfullinfo
    """

    id: int
    type: ChatType
    title: Optional[str]
    username: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    is_forum: Optional[bool]
    is_direct_messages: Optional[bool]
    accent_color_id: int
    max_reaction_count: int
    photo: Optional[ChatPhoto]
    active_usernames: Optional[List[str]]
    birthdate: Optional[Birthdate]
    business_intro: Optional[BusinessIntro]
    business_location: Optional[BusinessLocation]
    business_opening_hours: Optional[BusinessOpeningHours]
    personal_chat: Optional['chat.Chat']
    parent_chat: Optional['chat.Chat']
    available_reactions: Optional[List[ReactionType]]
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
    accepted_gift_types: Optional[AcceptedGiftTypes]
    can_send_paid_media: Optional[bool]
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
    rating: Optional[UserRating]
    first_profile_audio: Optional[Audio]
    unique_gift_colors: Optional[UniqueGiftColors]
    paid_message_star_count: Optional[int]
    guard_bot: Optional['chat.Chat']
    community: Optional[Community]

    @classmethod
    def parse(cls, data: Optional[Dict]) -> Optional['ChatFullInfo']:
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
            data.get('is_direct_messages'),
            data.get('accent_color_id', 0),
            data.get('max_reaction_count', 0),
            ChatPhoto.parse(data.get('photo')),
            data.get('active_usernames'),
            Birthdate.parse(data.get('birthdate')),
            BusinessIntro.parse(data.get('business_intro')),
            BusinessLocation.parse(data.get('business_location')),
            BusinessOpeningHours.parse(data.get('business_opening_hours')),
            chat.Chat.parse(data.get('personal_chat')),
            chat.Chat.parse(data.get('parent_chat')),
            [ReactionType.parse(r) for r in data['available_reactions']] if 'available_reactions' in data else None,
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
            AcceptedGiftTypes.parse(data.get('accepted_gift_types')),
            data.get('can_send_paid_media'),
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
            ChatLocation.parse(data.get('location')),
            UserRating.parse(data.get('rating')),
            Audio.parse(data.get('first_profile_audio')),
            UniqueGiftColors.parse(data.get('unique_gift_colors')),
            data.get('paid_message_star_count'),
            chat.Chat.parse(data.get('guard_bot')),
            Community.parse(data.get('community')),
        )
