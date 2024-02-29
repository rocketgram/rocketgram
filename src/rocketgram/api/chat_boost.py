# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional

from . import chat_boost_source


@dataclass(frozen=True)
class ChatBoost:
    """\
    Represents ChatBoost object:
    https://core.telegram.org/bots/api#chatboost
    """

    boost_id: str
    add_date: datetime
    expiration_date: datetime
    source: 'chat_boost_source.ChatBoostSource'

    @classmethod
    def parse(cls, data: dict) -> Optional['ChatBoost']:
        if data is None:
            return None

        return cls(
            data['boost_id'],
            datetime.fromtimestamp(data['add_date'], tz=timezone.utc),
            datetime.fromtimestamp(data['expiration_date'], tz=timezone.utc),
            chat_boost_source.ChatBoostSource.parse(data['source'])
        )
