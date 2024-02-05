# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass


@dataclass(frozen=True)
class MenuButton:
    """\
    Represents MenuButton object:
    https://core.telegram.org/bots/api#menubutton
    """
