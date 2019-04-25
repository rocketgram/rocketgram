# Copyright (C) 2015-2019 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from .keyboard import Keyboard
from ..types import InlineKeyboardMarkup, InlineKeyboardButton


class InlineKeyboard(Keyboard):
    __slots__ = ()

    def url(self, text, url) -> 'InlineKeyboard':
        self.add(InlineKeyboardButton(text=text, url=url))
        return self

    def callback(self, text, callback_data) -> 'InlineKeyboard':
        self.add(InlineKeyboardButton(text=text, callback_data=callback_data))
        return self

    def inline(self, text, switch_inline_query=str()) -> 'InlineKeyboard':
        self.add(InlineKeyboardButton(text=text, switch_inline_query=switch_inline_query))
        return self

    def inline_current(self, text, switch_inline_query_current_chat=str()) -> 'InlineKeyboard':
        self.add(InlineKeyboardButton(text=text, switch_inline_query_current_chat=switch_inline_query_current_chat))
        return self

    def game(self, text, callback_game) -> 'InlineKeyboard':
        self.add(InlineKeyboardButton(text=text, callback_game=callback_game))
        return self

    def pay(self, text) -> 'InlineKeyboard':
        self.add(InlineKeyboardButton(text=text, pay=True))
        return self

    def row(self) -> 'InlineKeyboard':
        return super().row()

    def render(self) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(super().render())
