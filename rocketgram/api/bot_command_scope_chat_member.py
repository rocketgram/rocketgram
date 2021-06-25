# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass, field
from typing import Union

from .bot_command_scope import BotCommandScope


@dataclass(frozen=True)
class BotCommandScopeChatMember(BotCommandScope):
    """\
    Represents BotCommandScopeChatMember object:
    https://core.telegram.org/bots/api#botcommandscopechatmember
    """

    type: str = field(init=False, default='chat_member')

    chat_id: Union[int, str]
    user_id: int
