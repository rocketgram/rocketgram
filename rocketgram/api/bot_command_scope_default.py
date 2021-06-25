# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass, field

from .bot_command_scope import BotCommandScope


@dataclass(frozen=True)
class BotCommandScopeDefault(BotCommandScope):
    """\
    Represents BotCommandScopeDefault object:
    https://core.telegram.org/bots/api#botcommandscopedefault
    """

    type: str = field(init=False, default='default')
