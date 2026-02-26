# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List

from .message_entity import MessageEntity
from .parse_mode_type import ParseModeType
from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class SendMessageDraft(BoolResultMixin, Request):
    """\
    Represents SendMessageDraft request object:
    https://core.telegram.org/bots/api#sendmessagedraft
    """

    chat_id: int
    draft_id: int
    text: str
    message_thread_id: Optional[int] = None
    parse_mode: Optional[ParseModeType] = None
    entities: Optional[List[MessageEntity]] = None
