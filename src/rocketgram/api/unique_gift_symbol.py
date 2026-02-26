# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .sticker import Sticker


@dataclass(frozen=True)
class UniqueGiftSymbol:
    """\
    Represents UniqueGiftSymbol object:
    https://core.telegram.org/bots/api#uniquegiftsymbol
    """

    name: str
    sticker: Sticker
    rarity_per_mille: int

    @classmethod
    def parse(cls, data: dict) -> Optional['UniqueGiftSymbol']:
        if data is None:
            return None

        return cls(
            data['name'],
            Sticker.parse(data['sticker']),
            data['rarity_per_mille'],
        )
