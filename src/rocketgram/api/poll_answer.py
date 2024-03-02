# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List

from .chat import Chat
from .user import User


@dataclass(frozen=True)
class PollAnswer:
    """\
    Represents PollAnswer object:
    https://core.telegram.org/bots/api#pollanswer

    """

    poll_id: str
    voter_chat: Optional[Chat]
    user: Optional[User]
    option_ids: List[int]

    @classmethod
    def parse(cls, data: dict) -> Optional['PollAnswer']:
        if data is None:
            return None

        return cls(
            data['poll_id'],
            Chat.parse(data.get('voter_chat')),
            User.parse(data.get('user')),
            data['option_ids']
        )
