# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from . import message
from .suggested_post_price import SuggestedPostPrice


@dataclass(frozen=True)
class SuggestedPostApproved:
    """\
    Represents SuggestedPostApproved object:
    https://core.telegram.org/bots/api#suggestedpostapproved
    """

    suggested_post_message: Optional['message.Message']
    price: Optional[SuggestedPostPrice]
    send_date: int

    @classmethod
    def parse(cls, data: dict) -> Optional['SuggestedPostApproved']:
        if data is None:
            return None

        return cls(
            message.Message.parse(data.get('suggested_post_message')),
            SuggestedPostPrice.parse(data.get('price')),
            data['send_date'],
        )
