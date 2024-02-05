# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass, field
from typing import Optional

from .inline_keyboard_markup import InlineKeyboardMarkup
from .inline_query_result import InlineQueryResult
from .input_message_content import InputMessageContent


@dataclass(frozen=True)
class InlineQueryResultArticle(InlineQueryResult):
    """\
    Represents InlineQueryResultArticle object:
    https://core.telegram.org/bots/api#inlinequeryresultarticle
    """

    type: str = field(init=False, default='article')

    id: str
    title: str
    input_message_content: InputMessageContent
    reply_markup: Optional[InlineKeyboardMarkup] = None
    url: Optional[str] = None
    hide_url: Optional[bool] = None
    description: Optional[str] = None
    thumbnail_url: Optional[str] = None
    thumbnail_width: Optional[int] = None
    thumbnail_height: Optional[int] = None
