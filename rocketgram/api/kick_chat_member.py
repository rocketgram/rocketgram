# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from datetime import datetime
from typing import Union, Optional

from .request import Request


@dataclass(frozen=True)
class KickChatMember(Request):
    """\
    Represents KickChatMember request object:
    https://core.telegram.org/bots/api#kickchatmember
    """

    method = "kickChatMember"

    chat_id: Union[int, str]
    user_id: int
    until_date: Optional[datetime] = None
