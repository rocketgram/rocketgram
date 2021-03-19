# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from datetime import datetime
from typing import Union, Optional

from .chat_permissions import ChatPermissions
from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class RestrictChatMember(BoolResultMixin, Request):
    """\
    Represents RestrictChatMember request object:
    https://core.telegram.org/bots/api#restrictchatmember
    """

    chat_id: Union[int, str]
    user_id: int
    permissions: ChatPermissions
    until_date: Optional[datetime] = None
