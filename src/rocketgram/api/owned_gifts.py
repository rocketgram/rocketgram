# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List

from .owned_gift import OwnedGift


@dataclass(frozen=True)
class OwnedGifts:
    """    Represents OwnedGifts object:
    https://core.telegram.org/bots/api#ownedgifts
    """

    total_count: int
    gifts: List[OwnedGift]
    next_offset: Optional[str]

    @classmethod
    def parse(cls, data: dict) -> Optional['OwnedGifts']:
        if data is None:
            return None

        return cls(
            data['total_count'],
            [OwnedGift.parse(g) for g in data['gifts']],
            data.get('next_offset')
        )
