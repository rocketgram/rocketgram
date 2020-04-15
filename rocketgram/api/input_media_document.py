# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass, field
from typing import Optional, Union

from .input_file import InputFile
from .input_media import InputMedia
from .parse_mode_type import ParseModeType


@dataclass(frozen=True)
class InputMediaDocument(InputMedia):
    """\
    Represents InputMediaDocument object:
    https://core.telegram.org/bots/api#inputmediadocument
    """

    type: str = field(init=False, default='document')

    media: Union[InputFile, str]
    thumb: Optional[Union[InputFile, str]] = None
    caption: Optional[str] = None
    parse_mode: Optional[ParseModeType] = None
