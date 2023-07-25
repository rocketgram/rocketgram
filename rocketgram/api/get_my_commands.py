# Copyright (C) 2015-2023 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Tuple, Optional

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

    scope: Optional[BotCommandScope] = None
    language_code: Optional[str] = None

    def parse_result(self, data) -> Tuple['api.BotCommand', ...]:
        assert isinstance(data, list), "Should be list."
        return tuple(api.BotCommand.parse(r) for r in data)

    async def send(self) -> Tuple['api.BotCommand', ...]:
        res = await context.bot.send(self)
        return res.result
