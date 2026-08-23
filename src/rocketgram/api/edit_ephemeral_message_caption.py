# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import List, Optional, Union

from .message_entity import MessageEntity
from .parse_mode_type import ParseModeType
from .request import Request
from .utils import AnyInlineKeyboard, BoolResultMixin


@dataclass(frozen=True)
class EditEphemeralMessageCaption(BoolResultMixin, Request):
    """\
    Represents EditEphemeralMessageCaption request object:
    https://core.telegram.org/bots/api#editephemeralmessagecaption
    """

    chat_id: Union[int, str]
    receiver_user_id: int
    ephemeral_message_id: int
    caption: Optional[str] = None
    parse_mode: Optional[ParseModeType] = None
    caption_entities: Optional[List[MessageEntity]] = None
    reply_markup: Optional[AnyInlineKeyboard] = None
