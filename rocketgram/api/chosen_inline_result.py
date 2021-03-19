# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .location import Location
from .user import User


@dataclass(frozen=True)
class ChosenInlineResult:
    """\
    Represents ChosenInlineResult object:
    https://core.telegram.org/bots/api#choseninlineresult

    Differences in field names:
    from -> user
    """

    result_id: str
    user: User
    location: Optional[Location]
    inline_message_id: Optional[str]
    query: str

    @classmethod
    def parse(cls, data: dict) -> Optional['ChosenInlineResult']:
        if data is None:
            return None

        return cls(data['result_id'], User.parse(data['from']), Location.parse(data.get('location')),
                   data.get('inline_message_id'), data['query'])
