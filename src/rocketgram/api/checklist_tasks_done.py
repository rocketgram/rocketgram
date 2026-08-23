# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List

from . import message


@dataclass(frozen=True)
class ChecklistTasksDone:
    """    Represents ChecklistTasksDone object:
    https://core.telegram.org/bots/api#checklisttasksdone
    """

    checklist_message: Optional['message.Message']
    marked_as_done_task_ids: Optional[List[int]]
    marked_as_not_done_task_ids: Optional[List[int]]

    @classmethod
    def parse(cls, data: dict) -> Optional['ChecklistTasksDone']:
        if data is None:
            return None

        return cls(
            message.Message.parse(data.get('checklist_message')),
            data.get('marked_as_done_task_ids'),
            data.get('marked_as_not_done_task_ids'),
        )
