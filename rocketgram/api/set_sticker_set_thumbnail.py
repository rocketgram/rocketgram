# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional, List

from .input_file import InputFile
from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class SetStickerSetThumbnail(BoolResultMixin, Request):
    """\
    Represents SetStickerSetThumbnail request object:
    https://core.telegram.org/bots/api#setstickersetthumbnail
    """

    name: str
    user_id: int
    thumbnail: Optional[Union[InputFile, str]] = None

    def files(self) -> List[InputFile]:
        if isinstance(self.thumbnail, InputFile):
            return [self.thumbnail]
        return list()
