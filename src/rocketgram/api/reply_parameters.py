# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List, Union

from . import message_entity
from .parse_mode_type import ParseModeType


@dataclass(frozen=True)
class ReplyParameters:
    """\
    Represents ReplyParameters object:
    https://core.telegram.org/bots/api#replyparameters
    """

    message_id: Optional[int] = None
    ephemeral_message_id: Optional[int] = None
    chat_id: Optional[Union[int, str]] = None
    allow_sending_without_reply: Optional[bool] = None
    quote: Optional[str] = None
    quote_parse_mode: Optional[ParseModeType] = None
    quote_entities: Optional[List['message_entity.MessageEntity']] = None
    quote_position: Optional[int] = None
    checklist_task_id: Optional[int] = None
    poll_option_id: Optional[str] = None
