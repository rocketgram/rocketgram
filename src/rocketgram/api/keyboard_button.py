# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .keyboard_button_poll_type import KeyboardButtonPollType
from .keyboard_button_request_chat import KeyboardButtonRequestChat
from .keyboard_button_request_users import KeyboardButtonRequestUsers
from .web_app_info import WebAppInfo


@dataclass(frozen=True)
class KeyboardButton:
    """\
    Represents KeyboardButton keyboard object:
    https://core.telegram.org/bots/api#keyboardbutton
    """

    text: str
    request_users: Optional[KeyboardButtonRequestUsers] = None
    request_chat: Optional[KeyboardButtonRequestChat] = None
    request_contact: Optional[bool] = None
    request_location: Optional[bool] = None
    request_poll: Optional[KeyboardButtonPollType] = None
    web_app: Optional[WebAppInfo] = None
