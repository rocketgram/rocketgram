# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass, field
from typing import List, Optional, Union

from .input_file import InputFile
from .input_media import InputMedia
from .message_entity import MessageEntity
from .parse_mode_type import ParseModeType


@dataclass(frozen=True)
class InputMediaVoiceNote(InputMedia):
    """\
    Represents InputMediaVoiceNote object:
    https://core.telegram.org/bots/api#inputmediavoicenote
    """

    type: str = field(init=False, default='voice_note')

    media: Union[InputFile, str]
    caption: Optional[str] = None
    parse_mode: Optional[ParseModeType] = None
    caption_entities: Optional[List[MessageEntity]] = None
    duration: Optional[int] = None
