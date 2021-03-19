# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .mask_position_point_type import MaskPositionPointType


@dataclass(frozen=True)
class MaskPosition:
    """\
    Represents MaskPosition object:
    https://core.telegram.org/bots/api#maskposition
    """

    point: str
    x_shift: float
    y_shift: float
    scale: float

    @classmethod
    def parse(cls, data: dict) -> Optional['MaskPosition']:
        if data is None:
            return None

        return cls(MaskPositionPointType(data['point']), data['x_shift'], data['y_shift'], data['scale'])
