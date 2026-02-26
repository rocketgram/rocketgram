# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class UniqueGiftBackdropColors:
    """\
    Represents UniqueGiftBackdropColors object:
    https://core.telegram.org/bots/api#uniquegiftbackdropcolors
    """

    center_color: int
    edge_color: int
    symbol_color: int
    text_color: int

    @classmethod
    def parse(cls, data: dict) -> Optional['UniqueGiftBackdropColors']:
        if data is None:
            return None

        return cls(
            data['center_color'],
            data['edge_color'],
            data['symbol_color'],
            data['text_color'],
        )
