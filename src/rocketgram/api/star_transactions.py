# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List

from .star_transaction import StarTransaction


@dataclass(frozen=True)
class StarTransactions:
    """\
    Represents StarTransactions object:
    https://core.telegram.org/bots/api#startransactions
    """

    transactions: List[StarTransaction]

    @classmethod
    def parse(cls, data: dict) -> Optional['StarTransactions']:
        if data is None:
            return None

        return cls([StarTransaction.parse(t) for t in data['transactions']])
