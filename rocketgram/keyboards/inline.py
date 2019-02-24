# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).


from .keyboard import Keyboard


class InlineKeyboard(Keyboard):
    def __init__(self):
        super().__init__()
        self._keyboard_type = 'inline_keyboard'

    def url(self, text, url):
        btn = {'text': text, 'url': url}
        self._buttons.append(btn)
        return self

    def callback(self, text, callback_data):
        btn = {'text': text, 'callback_data': callback_data}
        self._buttons.append(btn)
        return self

    def inline(self, text, switch_inline_query=str()):
        btn = {'text': text, 'switch_inline_query': switch_inline_query}
        self._buttons.append(btn)
        return self

    def inline_current(self, text, switch_inline_query_current_chat=str()):
        btn = {'text': text, 'switch_inline_query_current_chat': switch_inline_query_current_chat}
        self._buttons.append(btn)
        return self

    def game(self, text, callback_game):
        btn = {'text': text, 'callback_game': callback_game}
        self._buttons.append(btn)
        return self
