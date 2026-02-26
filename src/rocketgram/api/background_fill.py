# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List

from .background_fill_type import BackgroundFillType


@dataclass(frozen=True)
class BackgroundFill:
    """\
    Represents BackgroundFill, BackgroundFillSolid, BackgroundFillGradient, BackgroundFillFreeformGradient objects:
    https://core.telegram.org/bots/api#backgroundfill
    """

    type: BackgroundFillType
    color: Optional[int]
    top_color: Optional[int]
    bottom_color: Optional[int]
    rotation_angle: Optional[int]
    colors: Optional[List[int]]

    @classmethod
    def parse(cls, data: dict) -> Optional['BackgroundFill']:
        if data is None:
            return None

        try:
            fill_type = BackgroundFillType(data['type'])
        except ValueError:
            fill_type = BackgroundFillType.unknown

        return cls(
            fill_type,
            data.get('color'),
            data.get('top_color'),
            data.get('bottom_color'),
            data.get('rotation_angle'),
            data.get('colors'),
        )
