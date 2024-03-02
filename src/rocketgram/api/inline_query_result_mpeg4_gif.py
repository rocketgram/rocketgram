# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass, field
from typing import Optional, List

from .inline_keyboard_markup import InlineKeyboardMarkup
from .inline_query_result import InlineQueryResult
from .input_message_content import InputMessageContent
from .message_entity import MessageEntity
from .parse_mode_type import ParseModeType
from .thumbnail_mime_type import ThumbnailMimeType


@dataclass(frozen=True)
class InlineQueryResultMpeg4Gif(InlineQueryResult):
    """\
    Represents InlineQueryResultMpeg4Gif object:
    https://core.telegram.org/bots/api#inlinequeryresultmpeg4gif
    """

    type: str = field(init=False, default='mpeg4_gif')

    id: str
    mpeg4_url: str
    thumbnail_url: str
    thumbnail_mime_type: Optional[ThumbnailMimeType] = None
    mpeg4_width: Optional[int] = None
    mpeg4_height: Optional[int] = None
    mpeg4_duration: Optional[int] = None
    title: Optional[str] = None
    caption: Optional[str] = None
    parse_mode: Optional[ParseModeType] = None
    caption_entities: Optional[List[MessageEntity]] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional[InputMessageContent] = None
