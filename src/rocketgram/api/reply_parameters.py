# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List

from . import message_entity


@dataclass(frozen=True)
class ReplyParameters:
    """\
    Represents ReplyParameters object:
    https://core.telegram.org/bots/api#replyparameters
    """

    message_id: int
    chat_id: Optional[int] = None
    allow_sending_without_reply: Optional[bool] = None
    quote: Optional[str] = None
    quote_parse_mode: Optional[str] = None
    quote_entities: Optional[List['message_entity.MessageEntity']] = None
    quote_position: Optional[int] = None
