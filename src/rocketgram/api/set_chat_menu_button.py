# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .menu_button import MenuButton
from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class SetChatMenuButton(BoolResultMixin, Request):
    """\
    Represents SetChatMenuButton request object:
    https://core.telegram.org/bots/api#setchatmenubutton
    """

    chat_id: Optional[int] = None
    menu_button: Optional[MenuButton] = None
