# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional, List

from .input_file import InputFile
from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class SetStickerSetThumb(BoolResultMixin, Request):
    """\
    Represents SetStickerSetThumb request object:
    https://core.telegram.org/bots/api#setstickersetthumb
    """

    name: str
    user_id: int
    thumb: Optional[Union[InputFile, str]]

    def files(self) -> List[InputFile]:
        if isinstance(self.thumb, InputFile):
            return [self.thumb]
        return list()
