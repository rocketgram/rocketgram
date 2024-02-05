# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass, field

from .menu_button import MenuButton


@dataclass(frozen=True)
class MenuButtonDefault(MenuButton):
    """\
    Represents MenuButtonDefault object:
    https://core.telegram.org/bots/api#menubuttondefault
    """

    type: str = field(init=False, default='default')
