# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from . import message
from .suggested_post_price import SuggestedPostPrice


@dataclass(frozen=True)
class SuggestedPostApprovalFailed:
    """\
    Represents SuggestedPostApprovalFailed object:
    https://core.telegram.org/bots/api#suggestedpostapprovalfailed
    """

    suggested_post_message: Optional['message.Message']
    price: SuggestedPostPrice

    @classmethod
    def parse(cls, data: dict) -> Optional['SuggestedPostApprovalFailed']:
        if data is None:
            return None

        return cls(
            message.Message.parse(data.get('suggested_post_message')),
            SuggestedPostPrice.parse(data['price']),
        )
