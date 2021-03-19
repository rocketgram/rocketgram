# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from typing import Optional

from .keyboard import Keyboard
from .. import api


class InlineKeyboard(Keyboard):
    __slots__ = ()

    def url(self, text, url) -> 'InlineKeyboard':
        self.add(api.InlineKeyboardButton(text=text, url=url))
        return self

    def login(self, text: str, url: str, forward_text: Optional[str] = None, bot_username: Optional[str] = None,
              request_write_access: Optional[bool] = None) -> 'InlineKeyboard':
        lu = api.LoginUrl(url, forward_text, bot_username, request_write_access)
        self.add(api.InlineKeyboardButton(text=text, login_url=lu))
        return self

    def callback(self, text: str, callback_data: str) -> 'InlineKeyboard':
        self.add(api.InlineKeyboardButton(text=text, callback_data=callback_data))
        return self

    def inline(self, text: str, switch_inline_query: str = str()) -> 'InlineKeyboard':
        self.add(api.InlineKeyboardButton(text=text, switch_inline_query=switch_inline_query))
        return self

    def inline_current(self, text: str, switch_inline_query_current_chat: str = str()) -> 'InlineKeyboard':
        self.add(api.InlineKeyboardButton(text=text, switch_inline_query_current_chat=switch_inline_query_current_chat))
        return self

    def game(self, text: str, callback_game: str) -> 'InlineKeyboard':
        self.add(api.InlineKeyboardButton(text=text, callback_game=callback_game))
        return self

    def pay(self, text: str) -> 'InlineKeyboard':
        self.add(api.InlineKeyboardButton(text=text, pay=True))
        return self

    def row(self) -> 'InlineKeyboard':
        return super().row()

    def render(self) -> 'api.InlineKeyboardMarkup':
        return api.InlineKeyboardMarkup(self.render_buttons())
