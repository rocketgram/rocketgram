# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from . import chat
from . import chat_boost


@dataclass(frozen=True)
class ChatBoostUpdated:
    """\
    Represents ChatBoostUpdated object:
    https://core.telegram.org/bots/api#chatboostupdated
    """

    chat: 'chat.Chat'
    boost: 'chat_boost.ChatBoost'

    @classmethod
    def parse(cls, data: dict) -> Optional['ChatBoostUpdated']:
        if data is None:
            return None

        return cls(
            chat.Chat.parse(data['chat']),
            chat_boost.ChatBoost.parse(data['boost'])
        )
