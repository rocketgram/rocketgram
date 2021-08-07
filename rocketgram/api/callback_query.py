# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


import warnings
from dataclasses import dataclass
from typing import Optional

from .message import Message
from .user import User


@dataclass(frozen=True)
class CallbackQuery:
    """\
    Represents CallbackQuery object:
    https://core.telegram.org/bots/api#callbackquery

    Differences in field names:
    from -> user
    """

    id: str
    user: User
    message: Optional[Message]
    inline_message_id: Optional[str]
    chat_instance: str
    data: Optional[str]
    game_short_name: Optional[str]

    @classmethod
    def parse(cls, data: dict) -> Optional['CallbackQuery']:
        if data is None:
            return None

        return cls(data['id'], User.parse(data['from']), Message.parse(data.get('message')),
                   data.get('inline_message_id'), data['chat_instance'], data.get('data'), data.get('game_short_name'))

    @property
    def query_id(self) -> str:
        warnings.warn("This field is deprecated. Use `id` instead.", DeprecationWarning)

        return self.id
