# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .chat_type import ChatType
from .location import Location
from .user import User


@dataclass(frozen=True)
class InlineQuery:
    """\
    Represents InlineQuery object:
    https://core.telegram.org/bots/api#inlinequery

    Differences in field names:
    from -> user
    """

    id: str
    user: User
    location: Optional[Location]
    query: str
    offset: str
    chat_type: Optional[ChatType]

    @classmethod
    def parse(cls, data: dict) -> Optional['InlineQuery']:
        if data is None:
            return None

        try:
            chat_type = ChatType(data['chat_type'])
        except (ValueError, KeyError):
            chat_type = ChatType.unknown

        return cls(data['id'], User.parse(data['from']), Location.parse(data.get('location')),
                   data['query'], data['offset'], chat_type)
