# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional

from .request import Request
from .utils import ChatInviteLinkResultMixin


@dataclass(frozen=True)
class EditChatSubscriptionInviteLink(ChatInviteLinkResultMixin, Request):
    """    Represents EditChatSubscriptionInviteLink request object:
    https://core.telegram.org/bots/api#editchatsubscriptioninvitelink
    """

    chat_id: Union[int, str]
    invite_link: str
    name: Optional[str] = None
