# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List

from .input_file import InputFile
from .input_sticker import InputSticker
from .request import Request
from .sticker_type import StickerType
from .utils import BoolResultMixin


@dataclass(frozen=True)
class CreateNewStickerSet(BoolResultMixin, Request):
    """\
    Represents CreateNewStickerSet request object:
    https://core.telegram.org/bots/api#createnewstickerset
    """

    user_id: int
    name: str
    title: str
    stickers: List[InputSticker]
    sticker_type: Optional[StickerType] = None
    needs_repainting: Optional[bool] = None

    def files(self) -> List[InputFile]:
        files = list()
        for sticker in self.stickers:
            if isinstance(sticker.sticker, InputFile):
                files.append(sticker.sticker)
        return files
