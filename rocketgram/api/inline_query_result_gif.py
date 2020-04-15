# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass, field
from typing import Optional

from .inline_keyboard_markup import InlineKeyboardMarkup
from .inline_query_result import InlineQueryResult
from .parse_mode_type import ParseModeType
from .input_message_content import InputMessageContent


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
    gif_width: Optional[int] = None
    gif_height: Optional[int] = None
    gif_duration: Optional[int] = None
    title: Optional[str] = None
    caption: Optional[str] = None
    parse_mode: Optional[ParseModeType] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional[InputMessageContent] = None
