# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Tuple

from .input_file import InputFile
from .request import Request
from .sticker_format import StickerFormat
from .utils import FileResultMixin


@dataclass(frozen=True)
class UploadStickerFile(FileResultMixin, Request):
    """\
    Represents UploadStickerFile request object:
    https://core.telegram.org/bots/api#uploadstickerfile
    """

    user_id: int
    sticker: InputFile
    sticker_format: StickerFormat

    def files(self) -> Tuple[InputFile, ...]:
        return (self.sticker,) if isinstance(self.sticker, InputFile) else tuple()
