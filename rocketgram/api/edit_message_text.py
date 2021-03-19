# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional, List

from .message_entity import MessageEntity
from .parse_mode_type import ParseModeType
from .request import Request
from .utils import INLINE_KEYBOARDS, MessageOrBoolResultMixin


@dataclass(frozen=True)
class EditMessageText(MessageOrBoolResultMixin, Request):
    """\
    Represents EditMessageText request object:
    https://core.telegram.org/bots/api#editmessagetext
    """

    text: str
    chat_id: Optional[Union[int, str]] = None
    message_id: Optional[int] = None
    inline_message_id: Optional[str] = None
    parse_mode: Optional[ParseModeType] = None
    entities: Optional[List[MessageEntity]] = None
    disable_web_page_preview: Optional[bool] = None
    reply_markup: Optional[INLINE_KEYBOARDS] = None
