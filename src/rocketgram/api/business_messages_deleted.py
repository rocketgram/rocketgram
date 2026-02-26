# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List


@dataclass(frozen=True)
class BusinessMessagesDeleted:
    """\
    Represents BusinessMessagesDeleted object:
    https://core.telegram.org/bots/api#businessmessagesdeleted
    """

    business_connection_id: str
    chat: Optional[object]
    message_ids: List[int]

    @classmethod
    def parse(cls, data: dict) -> Optional['BusinessMessagesDeleted']:
        if data is None:
            return None

        from .chat import Chat

        return cls(
            data['business_connection_id'],
            Chat.parse(data['chat']),
            data['message_ids'],
        )
