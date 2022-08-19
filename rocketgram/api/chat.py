# Copyright (C) 2015-2022 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Dict, Optional

from . import message
from .chat_location import ChatLocation
from .chat_permissions import ChatPermissions
from .chat_photo import ChatPhoto
from .chat_type import ChatType


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
    photo: Optional[ChatPhoto]
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
    message_auto_delete_time: Optional[int]
    has_protected_content: Optional[bool]
    sticker_set_name: Optional[str]
    can_set_sticker_set: Optional[bool]
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

        return cls(data['id'], chat_type, data.get('title'), data.get('username'), data.get('first_name'),
                   data.get('last_name'), ChatPhoto.parse(data.get('photo')), data.get('bio'),
                   data.get('has_private_forwards'), data.get('has_restricted_voice_and_video_messages'),
                   data.get('join_to_send_messages'), data.get('join_by_request'), data.get('description'),
                   data.get('invite_link'), message.Message.parse(data.get('pinned_message')),
                   ChatPermissions.parse(data.get('permissions')), data.get('slow_mode_delay'),
                   data.get('message_auto_delete_time'), data.get('has_protected_content'),
                   data.get('sticker_set_name'), data.get('can_set_sticker_set'), data.get('linked_chat_id'),
                   ChatLocation.parse(data.get('location')))
