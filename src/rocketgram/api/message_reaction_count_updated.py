# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional, List

from . import chat
from . import reaction_count


@dataclass(frozen=True)
class MessageReactionCountUpdated:
    """\
    Represents MessageReactionCountUpdated object:
    https://core.telegram.org/bots/api#messagereactioncountupdated
    """

    chat: 'chat.Chat'
    message_id: int
    date: datetime
    reactions: List['reaction_count.ReactionCount']

    @classmethod
    def parse(cls, data: dict) -> Optional['MessageReactionCountUpdated']:
        if data is None:
            return None

        return cls(
            chat.Chat.parse(data['chat']),
            data['message_id'],
            datetime.fromtimestamp(data['date'], tz=timezone.utc),
            [reaction_count.ReactionCount.parse(rt) for rt in data['reactions']],
        )
