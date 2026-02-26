# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .transaction_partner import TransactionPartner


@dataclass(frozen=True)
class StarTransaction:
    """\
    Represents StarTransaction object:
    https://core.telegram.org/bots/api#startransaction
    """

    id: str
    amount: int
    nanostar_amount: Optional[int]
    date: int
    source: Optional[TransactionPartner]
    receiver: Optional[TransactionPartner]

    @classmethod
    def parse(cls, data: dict) -> Optional['StarTransaction']:
        if data is None:
            return None

        return cls(
            data['id'],
            data['amount'],
            data.get('nanostar_amount'),
            data['date'],
            TransactionPartner.parse(data.get('source')),
            TransactionPartner.parse(data.get('receiver')),
        )
