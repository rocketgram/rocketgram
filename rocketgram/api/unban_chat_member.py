# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from datetime import datetime
from typing import Union, Optional

from .request import Request


@dataclass(frozen=True)
class UnbanChatMember(Request):
    """\
    Represents UnbanChatMember request object:
    https://core.telegram.org/bots/api#unbanchatmember
    """

    method = "unbanChatMember"

    chat_id: Union[int, str]
    user_id: int
