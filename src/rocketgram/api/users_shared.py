# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List

from .shared_user import SharedUser


@dataclass(frozen=True)
class UsersShared:
    """\
    Represents UsersShared object:
    https://core.telegram.org/bots/api#usersshared
    """

    request_id: int
    users: List[SharedUser]

    @classmethod
    def parse(cls, data: dict) -> Optional['UsersShared']:
        if data is None:
            return None

        return cls(
            data['request_id'],
            [SharedUser.parse(u) for u in data['users']],
        )
