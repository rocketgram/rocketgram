# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass

from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class DeleteStickerFromSet(BoolResultMixin, Request):
    """\
    Represents DeleteStickerFromSet request object:
    https://core.telegram.org/bots/api#deletestickerfromset
    """

    sticker: str
