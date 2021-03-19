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
class InputMediaAudio(InputMedia):
    """\
    Represents InputMediaAudio object:
    https://core.telegram.org/bots/api#inputmediaaudio
    """

    type: str = field(init=False, default='audio')

    media: Union[InputFile, str]
    thumb: Optional[Union[InputFile, str]] = None
    caption: Optional[str] = None
    parse_mode: Optional[ParseModeType] = None
    caption_entities: Optional[List[MessageEntity]] = None
    duration: Optional[int] = None
    performer: Optional[str] = None
    title: Optional[str] = None
