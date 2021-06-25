# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import List, Optional

from .bot_command_scope import BotCommandScope
from .request import Request
from .. import api
from ..context import context


@dataclass(frozen=True)
class GetMyCommands(Request):
    """\
    Represents GetMyCommands request object:
    https://core.telegram.org/bots/api#getmycommands
    """

    scope: Optional[BotCommandScope]
    language_code: Optional[str]

    def parse_result(self, data) -> List['api.BotCommand']:
        assert isinstance(data, list), "Should be list."
        return [api.BotCommand.parse(r) for r in data]

    async def send(self) -> List['api.BotCommand']:
        res = await context.bot.send(self)
        return res.result
