# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .mask_position import MaskPosition
from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class SetStickerMaskPosition(BoolResultMixin, Request):
    """\
    Represents SetStickerMaskPosition request object:
    https://core.telegram.org/bots/api#setstickermaskposition
    """

    name: str
    mask_position: Optional[MaskPosition] = None
