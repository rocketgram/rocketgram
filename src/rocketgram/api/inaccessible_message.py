# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from . import chat


@dataclass(frozen=True)
class InaccessibleMessage:
    """    Represents InaccessibleMessage object:
    https://core.telegram.org/bots/api#inaccessiblemessage
    """

    chat: 'chat.Chat'
    message_id: int
    date: int

    @classmethod
    def parse(cls, data: dict) -> Optional['InaccessibleMessage']:
        if data is None:
            return None

        return cls(chat.Chat.parse(data['chat']), data['message_id'], data['date'])
