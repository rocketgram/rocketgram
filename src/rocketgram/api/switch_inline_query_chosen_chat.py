# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, Dict


@dataclass(frozen=True)
class SwitchInlineQueryChosenChat:
    """\
    Represents SwitchInlineQueryChosenChat keyboard object:
    https://core.telegram.org/bots/api#switchinlinequerychosenchat
    """

    query: Optional[str] = None
    allow_user_chats: Optional[bool] = None
    allow_bot_chats: Optional[bool] = None
    allow_group_chats: Optional[bool] = None
    allow_channel_chats: Optional[bool] = None

    @classmethod
    def parse(cls, data: Optional[Dict]) -> Optional['SwitchInlineQueryChosenChat']:
        if data is None:
            return None

        return cls(
            data.get('query'),
            data.get('allow_user_chats'),
            data.get('allow_bot_chats'),
            data.get('allow_group_chats'),
            data.get('allow_channel_chats'),
        )
