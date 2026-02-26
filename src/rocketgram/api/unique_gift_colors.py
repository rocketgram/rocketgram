# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List


@dataclass(frozen=True)
class UniqueGiftColors:
    """\
    Represents UniqueGiftColors object:
    https://core.telegram.org/bots/api#uniquegiftcolors
    """

    model_custom_emoji_id: str
    symbol_custom_emoji_id: str
    light_theme_main_color: int
    light_theme_other_colors: List[int]
    dark_theme_main_color: int
    dark_theme_other_colors: List[int]

    @classmethod
    def parse(cls, data: dict) -> Optional['UniqueGiftColors']:
        if data is None:
            return None

        return cls(
            data['model_custom_emoji_id'],
            data['symbol_custom_emoji_id'],
            data['light_theme_main_color'],
            data['light_theme_other_colors'],
            data['dark_theme_main_color'],
            data['dark_theme_other_colors'],
        )
