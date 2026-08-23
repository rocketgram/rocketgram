# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List

from .input_checklist_task import InputChecklistTask
from .message_entity import MessageEntity
from .parse_mode_type import ParseModeType


@dataclass(frozen=True)
class InputChecklist:
    """    Represents InputChecklist object:
    https://core.telegram.org/bots/api#inputchecklist
    """

    title: str
    tasks: List[InputChecklistTask]
    parse_mode: Optional[ParseModeType] = None
    title_entities: Optional[List[MessageEntity]] = None
    others_can_add_tasks: Optional[bool] = None
    others_can_mark_tasks_as_done: Optional[bool] = None
