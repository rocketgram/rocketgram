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
from .thumb_mime_type import ThumbMimeType


@dataclass(frozen=True)
class InlineQueryResultGif(InlineQueryResult):
    """\
    Represents InlineQueryResultGif object:
    https://core.telegram.org/bots/api#inlinequeryresultgif
    """

    type: str = field(init=False, default='gif')

    id: str
    gif_url: str
    thumb_url: str
    thumb_mime_type: Optional[ThumbMimeType] = None
    gif_width: Optional[int] = None
    gif_height: Optional[int] = None
    gif_duration: Optional[int] = None
    title: Optional[str] = None
    caption: Optional[str] = None
    parse_mode: Optional[ParseModeType] = None
    caption_entities: Optional[List[MessageEntity]] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional[InputMessageContent] = None
