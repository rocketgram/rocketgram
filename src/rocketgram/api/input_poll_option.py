# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List

from .message_entity import MessageEntity
from .parse_mode_type import ParseModeType
from .input_poll_option_media import InputPollOptionMedia


@dataclass(frozen=True)
class InputPollOption:
    """    Represents InputPollOption object:
    https://core.telegram.org/bots/api#inputpolloption
    """

    text: str
    text_parse_mode: Optional[ParseModeType] = None
    text_entities: Optional[List[MessageEntity]] = None
    media: Optional[InputPollOptionMedia] = None
