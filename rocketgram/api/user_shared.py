# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class UserShared:
    """\
    Represents UserShared object:
    https://core.telegram.org/bots/api#usershared
    """

    request_id: int
    user_id: int

    @classmethod
    def parse(cls, data: dict) -> Optional['UserShared']:
        if data is None:
            return None

        return cls(data['request_id'], data['user_id'])
