# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass, field

from .bot_command_scope import BotCommandScope


@dataclass(frozen=True)
class BotCommandScopeAllChatAdministrators(BotCommandScope):
    """\
    Represents BotCommandScopeAllChatAdministrators object:
    https://core.telegram.org/bots/api#botcommandscopeallchatadministrators
    """

    type: str = field(init=False, default='all_chat_administrators')
