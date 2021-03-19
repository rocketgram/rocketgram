# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, Dict

from .login_url import LoginUrl


@dataclass(frozen=True)
class InlineKeyboardButton:
    """\
    Represents InlineKeyboardButton keyboard object:
    https://core.telegram.org/bots/api#inlinekeyboardbutton
    """

    text: str
    url: Optional[str] = None
    login_url: Optional[LoginUrl] = None
    callback_data: Optional[str] = None
    switch_inline_query: Optional[str] = None
    switch_inline_query_current_chat: Optional[str] = None
    callback_game: Optional[str] = None
    pay: Optional[bool] = None

    @classmethod
    def parse(cls, data: Optional[Dict]) -> Optional['InlineKeyboardButton']:
        if data is None:
            return None

        if 'url' in data:
            return cls(data['text'], url=data['url'])
        if 'login_url' in data:
            return cls(data['text'], login_url=LoginUrl.parse(data['login_url']))
        if 'callback_data' in data:
            return cls(data['text'], callback_data=data['callback_data'])
        if 'switch_inline_query' in data:
            return cls(data['text'], switch_inline_query=data['switch_inline_query'])
        if 'switch_inline_query_current_chat' in data:
            return cls(data['text'], switch_inline_query_current_chat=data['switch_inline_query_current_chat'])
        if 'callback_game' in data:
            return cls(data['text'], callback_game=data['callback_game'])
        if 'pay' in data:
            return cls(data['text'], pay=data['pay'])
