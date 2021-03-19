# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union

from .request import Request
from .utils import ChatInviteLinkResultMixin


@dataclass(frozen=True)
class RevokeChatInviteLink(ChatInviteLinkResultMixin, Request):
    """\
    Represents RevokeChatInviteLink request object:
    https://core.telegram.org/bots/api#revokechatinvitelink
    """

    chat_id: Union[int, str]
    invite_link: str
