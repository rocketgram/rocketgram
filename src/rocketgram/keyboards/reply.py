# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from typing import Optional

from .keyboard import Keyboard
from .. import api


class ReplyKeyboard(Keyboard):
    __slots__ = ('__persistent', '__resize', '__one_time', '__placeholder', '__selective')

    def __init__(self, *,
                 persistent: bool = False,
                 resize: bool = True,
                 placeholder: Optional[str] = None,
                 one_time: bool = False,
                 selective: bool = False):
        super().__init__()

        self.__persistent = persistent
        self.__resize = resize
        self.__one_time = one_time
        self.__placeholder = placeholder
        self.__selective = selective

    def set_persistent(self, resize=False):
        self.__resize = resize

    persistent = property(fget=lambda self: self.__persistent, fset=set_persistent)

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

    def web(self, text: str, url: str) -> 'ReplyKeyboard':
        self.add(api.KeyboardButton(text=text, web_app=api.WebAppInfo(url=url)))
        return self

    def request_users(
            self,
            text: str,
            request_id: int,
            user_is_bot: Optional[bool] = None,
            user_is_premium: Optional[bool] = None,
            max_quantity: Optional[int] = None
    ) -> 'ReplyKeyboard':
        request_users = api.KeyboardButtonRequestUsers(
            request_id=request_id,
            user_is_bot=user_is_bot,
            user_is_premium=user_is_premium,
            max_quantity=max_quantity
        )
        self.add(api.KeyboardButton(text=text, request_users=request_users))
        return self

    def request_chat(
            self,
            text: str,
            request_id: int,
            chat_has_username: Optional[bool] = None,
            chat_is_created: Optional[bool] = None,
            user_administrator_rights: Optional['api.ChatAdministratorRights'] = None,
            bot_administrator_rights: Optional['api.ChatAdministratorRights'] = None,
            bot_is_member: Optional[bool] = None
    ) -> 'ReplyKeyboard':
        request_chat = api.KeyboardButtonRequestChat(
            request_id=request_id,
            chat_has_username=chat_has_username,
            chat_is_created=chat_is_created,
            user_administrator_rights=user_administrator_rights,
            bot_administrator_rights=bot_administrator_rights,
            bot_is_member=bot_is_member
        )
        self.add(api.KeyboardButton(text=text, request_chat=request_chat))
        return self

    def row(self) -> 'ReplyKeyboard':
        return super().row()

    def render(self) -> 'api.ReplyKeyboardMarkup':
        return api.ReplyKeyboardMarkup(
            self.render_buttons(),
            is_persistent=self.persistent if self.persistent else None,
            resize_keyboard=self.resize if self.resize else None,
            one_time_keyboard=self.one_time if self.one_time else None,
            input_field_placeholder=self.placeholder,
            selective=self.selective if self.selective else None
        )
