# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass

from .input_sticker import InputSticker
from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class ReplaceStickerInSet(BoolResultMixin, Request):
    """\
    Represents ReplaceStickerInSet request object:
    https://core.telegram.org/bots/api#replacestickerinset
    """

    user_id: int
    name: str
    old_sticker: str
    sticker: InputSticker
