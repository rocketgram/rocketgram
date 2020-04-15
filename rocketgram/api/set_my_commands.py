# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import List

from .request import Request
from .bot_command import BotCommand


@dataclass(frozen=True)
class SetMyCommands(Request):
    """\
    Represents SetMyCommands request object:
    https://core.telegram.org/bots/api#setmycommands
    """

    method = "setMyCommands"

    commands: List[BotCommand]
