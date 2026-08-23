# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass, field
from typing import Optional

from .input_media import InputMedia


@dataclass(frozen=True)
class InputMediaLocation(InputMedia):
    """\
    Represents InputMediaLocation object:
    https://core.telegram.org/bots/api#inputmedialocation
    """

    type: str = field(init=False, default='location')

    latitude: float
    longitude: float
    horizontal_accuracy: Optional[float] = None
