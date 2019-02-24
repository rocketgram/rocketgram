# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).


from .keyboard import Keyboard


class ReplyKeyboard(Keyboard):
    def __init__(self, *, selective=False, one_time=False, resize=False):
        super().__init__()
        self._keyboard_type = 'keyboard'
        self.set_selective(selective)
        self.set_one_time(one_time)
        self.set_resize(resize)

    def set_selective(self, selective=False):
        if selective:
            self._options['selective'] = True
        elif 'selective' in self._options:
            del self._options['selective']
        return self

    def set_one_time(self, one_time_keyboard=False):
        if one_time_keyboard:
            self._options['one_time_keyboard'] = True
        elif 'one_time_keyboard' in self._options:
            del self._options['one_time_keyboard']
        return self

    def set_resize(self, resize_keyboard=False):
        if resize_keyboard:
            self._options['resize_keyboard'] = True
        elif 'resize_keyboard' in self._options:
            del self._options['resize_keyboard']
        return self

    def text(self, text):
        btn = {'text': text}
        self._buttons.append(btn)
        return self

    def contact(self, text):
        btn = {'text': text, 'request_contact': True}
        self._buttons.append(btn)
        return self

    def location(self, text):
        btn = {'text': text, 'request_location': True}
        self._buttons.append(btn)
        return self
