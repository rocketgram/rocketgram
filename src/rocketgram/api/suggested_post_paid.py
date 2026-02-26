# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from . import message
from .star_amount import StarAmount


@dataclass(frozen=True)
class SuggestedPostPaid:
    """\
    Represents SuggestedPostPaid object:
    https://core.telegram.org/bots/api#suggestedpostpaid
    """

    suggested_post_message: Optional['message.Message']
    currency: str
    amount: Optional[int]
    star_amount: Optional[StarAmount]

    @classmethod
    def parse(cls, data: dict) -> Optional['SuggestedPostPaid']:
        if data is None:
            return None

        return cls(
            message.Message.parse(data.get('suggested_post_message')),
            data['currency'],
            data.get('amount'),
            StarAmount.parse(data.get('star_amount')),
        )
