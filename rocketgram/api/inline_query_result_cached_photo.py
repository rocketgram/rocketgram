# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass, field
from typing import Optional, List

from .inline_keyboard_markup import InlineKeyboardMarkup
from .inline_query_result import InlineQueryResult
from .input_message_content import InputMessageContent
from .message_entity import MessageEntity
from .parse_mode_type import ParseModeType


@dataclass(frozen=True)
class InlineQueryResultCachedPhoto(InlineQueryResult):
    """\
    Represents InlineQueryResultCachedPhoto object:
    https://core.telegram.org/bots/api#inlinequeryresultcachedphoto
    """

    type: str = field(init=False, default='photo')

    id: str
    photo_file_id: str
    title: Optional[str] = None
    description: Optional[str] = None
    caption: Optional[str] = None
    parse_mode: Optional[ParseModeType] = None
    caption_entities: Optional[List[MessageEntity]] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional[InputMessageContent] = None
