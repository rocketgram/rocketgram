# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional, List

from .message_entity import MessageEntity
from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class SendGift(BoolResultMixin, Request):
    """\
    Represents SendGift request object:
    https://core.telegram.org/bots/api#sendgift
    """

    gift_id: str
    user_id: Optional[int] = None
    chat_id: Optional[Union[int, str]] = None
    pay_for_upgrade: Optional[bool] = None
    text: Optional[str] = None
    text_parse_mode: Optional[str] = None
    text_entities: Optional[List[MessageEntity]] = None
