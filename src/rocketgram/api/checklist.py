# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List

from .checklist_task import ChecklistTask
from .message_entity import MessageEntity


@dataclass(frozen=True)
class Checklist:
    """    Represents Checklist object:
    https://core.telegram.org/bots/api#checklist
    """

    title: str
    title_entities: Optional[List[MessageEntity]]
    tasks: List[ChecklistTask]
    others_can_add_tasks: Optional[bool]
    others_can_mark_tasks_as_done: Optional[bool]

    @classmethod
    def parse(cls, data: dict) -> Optional['Checklist']:
        if data is None:
            return None

        return cls(
            data['title'],
            [MessageEntity.parse(e) for e in data['title_entities']] if 'title_entities' in data else None,
            [ChecklistTask.parse(t) for t in data['tasks']],
            data.get('others_can_add_tasks'),
            data.get('others_can_mark_tasks_as_done')
        )
