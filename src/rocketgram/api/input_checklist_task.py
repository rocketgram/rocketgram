# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List

from .message_entity import MessageEntity
from .parse_mode_type import ParseModeType


@dataclass(frozen=True)
class InputChecklistTask:
    """    Represents InputChecklistTask object:
    https://core.telegram.org/bots/api#inputchecklisttask
    """

    id: int
    text: str
    parse_mode: Optional[ParseModeType] = None
    text_entities: Optional[List[MessageEntity]] = None
