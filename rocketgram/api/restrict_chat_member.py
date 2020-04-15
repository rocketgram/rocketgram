# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from datetime import datetime
from typing import Union, Optional

from .request import Request
from .chat_permissions import ChatPermissions


@dataclass(frozen=True)
class RestrictChatMember(Request):
    """\
    Represents RestrictChatMember request object:
    https://core.telegram.org/bots/api#restrictchatmember
    """

    method = "restrictChatMember"

    chat_id: Union[int, str]
    user_id: int
    permissions: ChatPermissions
    until_date: Optional[datetime] = None
