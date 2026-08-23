# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List

from . import chat
from . import user
from .gift import Gift
from .message_entity import MessageEntity
from .owned_gift_type import OwnedGiftType
from .unique_gift import UniqueGift


@dataclass(frozen=True)
class OwnedGift:
    """    Represents OwnedGift, OwnedGiftRegular, OwnedGiftUnique objects:
    https://core.telegram.org/bots/api#ownedgift
    """

    type: OwnedGiftType
    gift: Optional[Gift]
    unique_gift: Optional[UniqueGift]
    owned_gift_id: Optional[str]
    sender_user: Optional['user.User']
    send_date: Optional[int]
    text: Optional[str]
    entities: Optional[List[MessageEntity]]
    is_private: Optional[bool]
    is_saved: Optional[bool]
    can_be_upgraded: Optional[bool]
    was_refunded: Optional[bool]
    convert_star_count: Optional[int]
    prepaid_upgrade_star_count: Optional[int]
    title: Optional[str]
    number: Optional[int]
    transfer_star_count: Optional[int]
    next_transfer_date: Optional[int]
    seller_chat: Optional['chat.Chat']

    @classmethod
    def parse(cls, data: dict) -> Optional['OwnedGift']:
        if data is None:
            return None

        try:
            gift_type = OwnedGiftType(data['type'])
        except ValueError:
            gift_type = OwnedGiftType.unknown

        return cls(
            gift_type,
            Gift.parse(data.get('gift')),
            UniqueGift.parse(data.get('unique_gift')),
            data.get('owned_gift_id'),
            user.User.parse(data.get('sender_user')),
            data.get('send_date'),
            data.get('text'),
            [MessageEntity.parse(e) for e in data['entities']] if 'entities' in data else None,
            data.get('is_private'),
            data.get('is_saved'),
            data.get('can_be_upgraded'),
            data.get('was_refunded'),
            data.get('convert_star_count'),
            data.get('prepaid_upgrade_star_count'),
            data.get('title'),
            data.get('number'),
            data.get('transfer_star_count'),
            data.get('next_transfer_date'),
            chat.Chat.parse(data.get('seller_chat'))
        )
