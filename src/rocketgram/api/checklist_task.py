# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List

from . import chat
from . import user
from .message_entity import MessageEntity


@dataclass(frozen=True)
class ChecklistTask:
    """    Represents ChecklistTask object:
    https://core.telegram.org/bots/api#checklisttask
    """

    id: int
    text: str
    text_entities: Optional[List[MessageEntity]]
    completed_by_user: Optional['user.User']
    completed_by_chat: Optional['chat.Chat']
    completion_date: Optional[int]

    @classmethod
    def parse(cls, data: dict) -> Optional['ChecklistTask']:
        if data is None:
            return None

        return cls(
            data['id'],
            data['text'],
            [MessageEntity.parse(e) for e in data['text_entities']] if 'text_entities' in data else None,
            user.User.parse(data.get('completed_by_user')),
            chat.Chat.parse(data.get('completed_by_chat')),
            data.get('completion_date')
        )
