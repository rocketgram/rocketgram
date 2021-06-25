# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import List, Optional

from .bot_command_scope import BotCommandScope
from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class DeleteMyCommands(BoolResultMixin, Request):
    """\
    Represents DeleteMyCommands request object:
    https://core.telegram.org/bots/api#deletemycommands
    """

    scope: Optional[List[BotCommandScope]]
    language_code: Optional[str]
