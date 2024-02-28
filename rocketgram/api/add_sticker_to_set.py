# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import List

from .input_file import InputFile
from .input_sticker import InputSticker
from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class AddStickerToSet(BoolResultMixin, Request):
    """\
    Represents AddStickerToSet request object:
    https://core.telegram.org/bots/api#addstickertoset
    """

    user_id: int
    name: str
    sticker: InputSticker

    def files(self) -> List[InputFile]:
        if isinstance(self.sticker.sticker, InputFile):
            return [self.sticker.sticker]
        return list()
