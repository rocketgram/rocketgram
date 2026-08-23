# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List

from .message_entity import MessageEntity
from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class GiftPremiumSubscription(BoolResultMixin, Request):
    """    Represents GiftPremiumSubscription request object:
    https://core.telegram.org/bots/api#giftpremiumsubscription
    """

    user_id: int
    month_count: int
    star_count: int
    text: Optional[str] = None
    text_parse_mode: Optional[str] = None
    text_entities: Optional[List[MessageEntity]] = None
