# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List

from .gift import Gift
from .message_entity import MessageEntity


@dataclass(frozen=True)
class GiftInfo:
    """\
    Represents GiftInfo object:
    https://core.telegram.org/bots/api#giftinfo
    """

    gift: Gift
    owned_gift_id: Optional[str]
    convert_star_count: Optional[int]
    prepaid_upgrade_star_count: Optional[int]
    is_upgrade_separate: Optional[bool]
    can_be_upgraded: Optional[bool]
    text: Optional[str]
    entities: Optional[List[MessageEntity]]
    is_private: Optional[bool]
    unique_gift_number: Optional[int]

    @classmethod
    def parse(cls, data: dict) -> Optional['GiftInfo']:
        if data is None:
            return None

        return cls(
            Gift.parse(data['gift']),
            data.get('owned_gift_id'),
            data.get('convert_star_count'),
            data.get('prepaid_upgrade_star_count'),
            data.get('is_upgrade_separate'),
            data.get('can_be_upgraded'),
            data.get('text'),
            [MessageEntity.parse(e) for e in data['entities']] if 'entities' in data else None,
            data.get('is_private'),
            data.get('unique_gift_number')
        )

