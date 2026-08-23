# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from . import chat
from .gift_background import GiftBackground
from .sticker import Sticker


@dataclass(frozen=True)
class Gift:
    """\
    Represents Gift object:
    https://core.telegram.org/bots/api#gift
    """

    id: str
    sticker: Sticker
    star_count: int
    upgrade_star_count: Optional[int]
    is_premium: Optional[bool]
    has_colors: Optional[bool]
    total_count: Optional[int]
    remaining_count: Optional[int]
    personal_total_count: Optional[int]
    personal_remaining_count: Optional[int]
    background: Optional[GiftBackground]
    unique_gift_variant_count: Optional[int]
    publisher_chat: Optional['chat.Chat']

    @classmethod
    def parse(cls, data: dict) -> Optional['Gift']:
        if data is None:
            return None

        return cls(
            data['id'],
            Sticker.parse(data['sticker']),
            data['star_count'],
            data.get('upgrade_star_count'),
            data.get('is_premium'),
            data.get('has_colors'),
            data.get('total_count'),
            data.get('remaining_count'),
            data.get('personal_total_count'),
            data.get('personal_remaining_count'),
            GiftBackground.parse(data.get('background')),
            data.get('unique_gift_variant_count'),
            chat.Chat.parse(data.get('publisher_chat'))
        )

