# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .location import Location
from .user import User


@dataclass(frozen=True)
class InlineQuery:
    """\
    Represents InlineQuery object:
    https://core.telegram.org/bots/api#inlinequery

    Differences in field names:
    id -> query_id
    from -> user
    """

    query_id: str
    user: User
    location: Optional[Location]
    query: str
    offset: str

    @classmethod
    def parse(cls, data: dict) -> Optional['InlineQuery']:
        if data is None:
            return None

        return cls(data['id'], User.parse(data['from']), Location.parse(data.get('location')),
                   data['query'], data['offset'])
