# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .sticker import Sticker


@dataclass(frozen=True)
class BusinessIntro:
    """\
    Represents BusinessIntro object:
    https://core.telegram.org/bots/api#businessintro
    """

    title: Optional[str]
    message: Optional[str]
    sticker: Optional[Sticker]

    @classmethod
    def parse(cls, data: dict) -> Optional['BusinessIntro']:
        if data is None:
            return None

        return cls(
            data.get('title'),
            data.get('message'),
            Sticker.parse(data.get('sticker')),
        )
