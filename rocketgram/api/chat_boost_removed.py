# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional

from . import chat
from . import chat_boost_source


@dataclass(frozen=True)
class ChatBoostRemoved:
    """\
    Represents ChatBoostRemoved object:
    https://core.telegram.org/bots/api#chatboostremoved
    """

    chat: 'chat.Chat'
    boost_id: str
    remove_date: datetime
    source: 'chat_boost_source.ChatBoostSource'

    @classmethod
    def parse(cls, data: dict) -> Optional['ChatBoostRemoved']:
        if data is None:
            return None

        return cls(
            chat.Chat.parse(data['chat']),
            data['boost_id'],
            datetime.fromtimestamp(data['remove_date'], tz=timezone.utc),
            chat_boost_source.ChatBoostSource.parse(data['source'])
        )
