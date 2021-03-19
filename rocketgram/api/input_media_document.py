# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass, field
from typing import Optional, Union, List

from .input_file import InputFile
from .input_media import InputMedia
from .message_entity import MessageEntity
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
    caption_entities: Optional[List[MessageEntity]] = None
    disable_content_type_detection: Optional[bool] = None
