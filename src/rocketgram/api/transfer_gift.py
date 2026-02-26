# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class TransferGift(BoolResultMixin, Request):
    """\
    Represents TransferGift request object:
    https://core.telegram.org/bots/api#transfergift
    """

    business_connection_id: str
    owned_gift_id: str
    new_owner_chat_id: int
    star_count: Optional[int] = None
