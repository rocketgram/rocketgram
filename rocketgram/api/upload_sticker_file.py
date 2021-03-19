# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import List

from .input_file import InputFile
from .request import Request
from .utils import FileResultMixin


@dataclass(frozen=True)
class UploadStickerFile(FileResultMixin, Request):
    """\
    Represents UploadStickerFile request object:
    https://core.telegram.org/bots/api#uploadstickerfile
    """

    user_id: int
    png_sticker: InputFile

    def files(self) -> List[InputFile]:
        if isinstance(self.png_sticker, InputFile):
            return [self.png_sticker]
        return list()
