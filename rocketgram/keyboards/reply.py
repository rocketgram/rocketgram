# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from typing import Optional

from .keyboard import Keyboard
from .. import api


class ReplyKeyboard(Keyboard):
    __slots__ = ('__resize', '__one_time', '__placeholder', '__selective')

    def __init__(self, *, resize: bool = True, placeholder: Optional[str] = None, one_time: bool = False,
                 selective: bool = False):
        super().__init__()

        self.__resize = resize
        self.__one_time = one_time
        self.__placeholder = placeholder
        self.__selective = selective

    def set_resize(self, resize=False):
        self.__resize = resize

    resize = property(fget=lambda self: self.__resize, fset=set_resize)

    def set_one_time(self, one_time=False):
        self.__one_time = one_time

    one_time = property(fget=lambda self: self.__one_time, fset=set_one_time)

    def set_placeholder(self, placeholder: Optional[str] = None):
        self.__placeholder = placeholder

    placeholder = property(fget=lambda self: self.__placeholder, fset=set_placeholder)

    def set_selective(self, selective=False):
        self.__selective = selective

    selective = property(fget=lambda self: self.__selective, fset=set_selective)

    def text(self, text: str) -> 'ReplyKeyboard':
        self.add(api.KeyboardButton(text=text))
        return self

    def contact(self, text: str) -> 'ReplyKeyboard':
        self.add(api.KeyboardButton(text=text, request_contact=True))
        return self

    def location(self, text: str) -> 'ReplyKeyboard':
        self.add(api.KeyboardButton(text=text, request_location=True))
        return self

    def poll(self, text: str, request_poll: 'api.PollType') -> 'ReplyKeyboard':
        self.add(api.KeyboardButton(text=text, request_poll=api.KeyboardButtonPollType(request_poll)))
        return self

    def row(self) -> 'ReplyKeyboard':
        return super().row()

    def render(self) -> 'api.ReplyKeyboardMarkup':
        return api.ReplyKeyboardMarkup(self.render_buttons(),
                                       resize_keyboard=self.resize if self.resize else None,
                                       one_time_keyboard=self.one_time if self.one_time else None,
                                       input_field_placeholder=self.placeholder,
                                       selective=self.selective if self.selective else None)
