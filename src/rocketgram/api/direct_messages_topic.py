# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .user import User


@dataclass(frozen=True)
class DirectMessagesTopic:
    """\
    Represents DirectMessagesTopic object:
    https://core.telegram.org/bots/api#directmessagestopic
    """

    topic_id: int
    user: Optional[User]

    @classmethod
    def parse(cls, data: dict) -> Optional['DirectMessagesTopic']:
        if data is None:
            return None

        return cls(
            data['topic_id'],
            User.parse(data.get('user')),
        )
