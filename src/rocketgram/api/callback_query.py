# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, Union

from .inaccessible_message import InaccessibleMessage
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
    message: Optional[Union[Message, InaccessibleMessage]]
    inline_message_id: Optional[str]
    chat_instance: str
    data: Optional[str]
    game_short_name: Optional[str]

    @classmethod
    def parse(cls, data: dict) -> Optional['CallbackQuery']:
        if data is None:
            return None

        message_data = data.get('message')
        message = None
        if message_data is not None:
            message = InaccessibleMessage.parse(message_data) \
                if message_data.get('date') == 0 else Message.parse(message_data)

        return cls(data['id'], User.parse(data['from']), message,
                   data.get('inline_message_id'), data['chat_instance'], data.get('data'), data.get('game_short_name'))
