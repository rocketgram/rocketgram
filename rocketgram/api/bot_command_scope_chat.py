# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass, field
from typing import Union

from .bot_command_scope import BotCommandScope


@dataclass(frozen=True)
class BotCommandScopeChat(BotCommandScope):
    """\
    Represents BotCommandScopeChat object:
    https://core.telegram.org/bots/api#botcommandscopechat
    """

    type: str = field(init=False, default='chat')
    
    chat_id: Union[int, str]
