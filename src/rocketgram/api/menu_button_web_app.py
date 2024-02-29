# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass, field

from .menu_button import MenuButton
from .web_app_info import WebAppInfo


@dataclass(frozen=True)
class MenuButtonWebApp(MenuButton):
    """\
    Represents MenuButtonWebApp object:
    https://core.telegram.org/bots/api#menubuttonwebapp
    """

    type: str = field(init=False, default='web_app')

    text: str
    web_app: WebAppInfo
