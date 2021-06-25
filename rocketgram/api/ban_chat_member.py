# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from datetime import datetime
from typing import Union, Optional

from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class BanChatMember(BoolResultMixin, Request):
    """\
    Represents BanChatMember request object:
    https://core.telegram.org/bots/api#banchatmember
    """

    chat_id: Union[int, str]
    user_id: int
    until_date: Optional[datetime] = None
    revoke_messages: Optional[bool] = None


KickChatMember = BanChatMember  # Deprecated! Will be removed in version 4.
