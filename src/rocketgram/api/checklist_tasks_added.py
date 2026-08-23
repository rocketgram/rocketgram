# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List

from . import message
from .checklist_task import ChecklistTask


@dataclass(frozen=True)
class ChecklistTasksAdded:
    """    Represents ChecklistTasksAdded object:
    https://core.telegram.org/bots/api#checklisttasksadded
    """

    checklist_message: Optional['message.Message']
    tasks: List[ChecklistTask]

    @classmethod
    def parse(cls, data: dict) -> Optional['ChecklistTasksAdded']:
        if data is None:
            return None

        return cls(
            message.Message.parse(data.get('checklist_message')),
            [ChecklistTask.parse(t) for t in data['tasks']]
        )
