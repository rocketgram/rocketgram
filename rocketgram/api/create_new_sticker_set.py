# Copyright (C) 2015-2022 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional, List

from .input_file import InputFile
from .mask_position import MaskPosition
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
    emojis: str
    png_sticker: Optional[Union[InputFile, str]] = None
    tgs_sticker: Optional[InputFile] = None
    webm_sticker: Optional[InputFile] = None
    contains_masks: Optional[bool] = None  # deprecated
    sticker_type: Optional[StickerType] = None
    mask_position: Optional[MaskPosition] = None

    def files(self) -> List[InputFile]:
        files = list()
        if isinstance(self.png_sticker, InputFile):
            files.append(self.png_sticker)
        if self.tgs_sticker is not None:
            files.append(self.tgs_sticker)
        return files
