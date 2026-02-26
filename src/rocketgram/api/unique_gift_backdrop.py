# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .unique_gift_backdrop_colors import UniqueGiftBackdropColors


@dataclass(frozen=True)
class UniqueGiftBackdrop:
    """\
    Represents UniqueGiftBackdrop object:
    https://core.telegram.org/bots/api#uniquegiftbackdrop
    """

    name: str
    colors: UniqueGiftBackdropColors
    rarity_per_mille: int

    @classmethod
    def parse(cls, data: dict) -> Optional['UniqueGiftBackdrop']:
        if data is None:
            return None

        return cls(
            data['name'],
            UniqueGiftBackdropColors.parse(data['colors']),
            data['rarity_per_mille'],
        )
