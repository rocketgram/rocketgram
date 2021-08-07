# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import List, Optional

from .bot_command import BotCommand
from .bot_command_scope import BotCommandScope
from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class SetMyCommands(BoolResultMixin, Request):
    """\
    Represents SetMyCommands request object:
    https://core.telegram.org/bots/api#setmycommands
    """

    commands: List[BotCommand]
    scope: Optional[BotCommandScope] = None
    language_code: Optional[str] = None
