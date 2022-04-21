# Copyright (C) 2015-2022 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .keyboard_button_poll_type import KeyboardButtonPollType
from .web_app_info import WebAppInfo


@dataclass(frozen=True)
class KeyboardButton:
    """\
    Represents KeyboardButton keyboard object:
    https://core.telegram.org/bots/api#keyboardbutton
    """

    text: str
    request_contact: Optional[bool] = None
    request_location: Optional[bool] = None
    request_poll: Optional[KeyboardButtonPollType] = None
    web_app: Optional[WebAppInfo] = None
