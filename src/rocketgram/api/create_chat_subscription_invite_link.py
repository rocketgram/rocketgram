# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional

from .request import Request
from .utils import ChatInviteLinkResultMixin


@dataclass(frozen=True)
class CreateChatSubscriptionInviteLink(ChatInviteLinkResultMixin, Request):
    """    Represents CreateChatSubscriptionInviteLink request object:
    https://core.telegram.org/bots/api#createchatsubscriptioninvitelink
    """

    chat_id: Union[int, str]
    subscription_period: int
    subscription_price: int
    name: Optional[str] = None
