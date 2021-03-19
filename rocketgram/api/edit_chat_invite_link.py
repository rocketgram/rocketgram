# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from datetime import datetime
from typing import Union, Optional

from .request import Request
from .utils import ChatInviteLinkResultMixin


@dataclass(frozen=True)
class EditChatInviteLink(ChatInviteLinkResultMixin, Request):
    """\
    Represents EditChatInviteLink request object:
    https://core.telegram.org/bots/api#editchatinvitelink
    """

    chat_id: Union[int, str]
    invite_link: str
    expire_date: Optional[datetime] = None
    member_limit: Optional[int] = None
