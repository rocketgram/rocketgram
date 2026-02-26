# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .unique_gift import UniqueGift


@dataclass(frozen=True)
class UniqueGiftInfo:
    """\
    Represents UniqueGiftInfo object:
    https://core.telegram.org/bots/api#uniquegiftinfo
    """

    gift: UniqueGift
    origin: str
    last_resale_currency: Optional[str]
    last_resale_amount: Optional[int]
    owned_gift_id: Optional[str]
    transfer_star_count: Optional[int]
    next_transfer_date: Optional[int]

    @classmethod
    def parse(cls, data: dict) -> Optional['UniqueGiftInfo']:
        if data is None:
            return None

        return cls(
            UniqueGift.parse(data['gift']),
            data['origin'],
            data.get('last_resale_currency'),
            data.get('last_resale_amount'),
            data.get('owned_gift_id'),
            data.get('transfer_star_count'),
            data.get('next_transfer_date'),
        )
