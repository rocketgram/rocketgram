# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional, List

from . import chat
from . import reaction_type
from . import user


@dataclass(frozen=True)
class MessageReactionUpdated:
    """\
    Represents MessageReactionUpdated object:
    https://core.telegram.org/bots/api#messagereactionupdated
    """

    chat: 'chat.Chat'
    message_id: int
    user: Optional['user.User']
    actor_chat: Optional['chat.Chat']
    date: datetime
    old_reaction: List['reaction_type.ReactionType']
    new_reaction: List['reaction_type.ReactionType']

    @classmethod
    def parse(cls, data: dict) -> Optional['MessageReactionUpdated']:
        if data is None:
            return None

        return cls(
            chat.Chat.parse(data['chat']),
            data['message_id'],
            user.User.parse(data.get('user')),
            chat.Chat.parse(data.get('actor_chat')),
            datetime.fromtimestamp(data['date'], tz=timezone.utc),
            [reaction_type.ReactionType.parse(rt) for rt in data['old_reaction']],
            [reaction_type.ReactionType.parse(rt) for rt in data['new_reaction']]
        )
