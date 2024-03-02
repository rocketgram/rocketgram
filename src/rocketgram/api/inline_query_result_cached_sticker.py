# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass, field
from typing import Optional

from .inline_keyboard_markup import InlineKeyboardMarkup
from .inline_query_result import InlineQueryResult
from .input_message_content import InputMessageContent


@dataclass(frozen=True)
class InlineQueryResultCachedSticker(InlineQueryResult):
    """\
    Represents InlineQueryResultCachedSticker object:
    https://core.telegram.org/bots/api#inlinequeryresultcachedsticker
    """

    type: str = field(init=False, default='sticker')

    id: str
    sticker_file_id: str
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional[InputMessageContent] = None
