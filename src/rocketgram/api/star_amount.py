# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class StarAmount:
    """\
    Represents StarAmount object:
    https://core.telegram.org/bots/api#staramount
    """

    amount: int
    nanostar_amount: Optional[int]

    @classmethod
    def parse(cls, data: dict) -> Optional['StarAmount']:
        if data is None:
            return None

        return cls(
            data['amount'],
            data.get('nanostar_amount'),
        )
