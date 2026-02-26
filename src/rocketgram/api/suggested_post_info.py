# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .suggested_post_price import SuggestedPostPrice


@dataclass(frozen=True)
class SuggestedPostInfo:
    """\
    Represents SuggestedPostInfo object:
    https://core.telegram.org/bots/api#suggestedpostinfo
    """

    state: str
    price: Optional[SuggestedPostPrice]
    send_date: Optional[int]

    @classmethod
    def parse(cls, data: dict) -> Optional['SuggestedPostInfo']:
        if data is None:
            return None

        return cls(
            data['state'],
            SuggestedPostPrice.parse(data.get('price')),
            data.get('send_date'),
        )
