# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional, List

from .request import Request
from .utils import BoolResultMixin
from .. import api


@dataclass(frozen=True)
class AddStickerToSet(BoolResultMixin, Request):
    """\
    Represents AddStickerToSet request object:
    https://core.telegram.org/bots/api#addstickertoset
    """

    user_id: int
    name: str
    png_sticker: Optional[Union['api.InputFile', str]]
    tgs_sticker: Optional['api.InputFile']
    emojis: str
    mask_position: Optional['api.MaskPosition'] = None

    def files(self) -> List['api.InputFile']:
        files = list()
        if isinstance(self.png_sticker, api.InputFile):
            files.append(self.png_sticker)
        if self.tgs_sticker is not None:
            files.append(self.tgs_sticker)
        return files
