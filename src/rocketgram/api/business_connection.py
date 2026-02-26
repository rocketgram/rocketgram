# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .business_bot_rights import BusinessBotRights
from .user import User


@dataclass(frozen=True)
class BusinessConnection:
    """\
    Represents BusinessConnection object:
    https://core.telegram.org/bots/api#businessconnection
    """

    id: str
    user: User
    user_chat_id: int
    date: int
    rights: Optional[BusinessBotRights]
    is_enabled: Optional[bool]

    @classmethod
    def parse(cls, data: dict) -> Optional['BusinessConnection']:
        if data is None:
            return None

        return cls(
            data['id'],
            User.parse(data['user']),
            data['user_chat_id'],
            data['date'],
            BusinessBotRights.parse(data.get('rights')),
            data.get('is_enabled'),
        )
