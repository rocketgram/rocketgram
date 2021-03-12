# Copyright (C) 2015-2020 by Vd.
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

    Differences in field names:
    id -> chat_id
    type -> chat_type
    """

    chat_id: int
    chat_type: ChatType
    title: Optional[str]
    username: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    photo: Optional[ChatPhoto]
    bio: Optional[str]
    description: Optional[str]
    invite_link: Optional[str]
    pinned_message: Optional['message.Message']
    permissions: Optional[ChatPermissions]
    slow_mode_delay: Optional[int]
    sticker_set_name: Optional[str]
    can_set_sticker_set: Optional[bool]
    linked_chat_id: Optional[int]
    location: Optional[ChatLocation]

    @classmethod
    def parse(cls, data: Optional[Dict]) -> Optional['Chat']:
        if data is None:
            return None

        return cls(data['id'], ChatType(data['type']), data.get('title'), data.get('username'), data.get('first_name'),
                   data.get('last_name'), ChatPhoto.parse(data.get('photo')), data.get('bio'), data.get('description'),
                   data.get('invite_link'), message.Message.parse(data.get('pinned_message')),
                   ChatPermissions.parse(data.get('permissions')), data.get('slow_mode_delay'),
                   data.get('sticker_set_name'), data.get('can_set_sticker_set'), data.get('linked_chat_id'),
                   ChatLocation.parse(data.get('location')))
