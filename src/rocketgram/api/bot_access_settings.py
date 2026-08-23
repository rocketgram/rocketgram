# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import List, Optional

from .user import User


@dataclass(frozen=True)
class BotAccessSettings:
    """\
    Represents BotAccessSettings object:
    https://core.telegram.org/bots/api#botaccesssettings
    """

    is_access_restricted: bool
    added_users: Optional[List[User]]

    @classmethod
    def parse(cls, data: dict) -> Optional['BotAccessSettings']:
        if data is None:
            return None

        return cls(
            data['is_access_restricted'],
            [User.parse(d) for d in data['added_users']] if 'added_users' in data else None,
        )
