# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass, field
from typing import Optional

from .inline_keyboard_markup import InlineKeyboardMarkup
from .inline_query_result import InlineQueryResult


@dataclass(frozen=True)
class InlineQueryResultGame(InlineQueryResult):
    """\
    Represents InlineQueryResultGame object:
    https://core.telegram.org/bots/api#inlinequeryresultgame
    """

    type: str = field(init=False, default='game')

    id: str
    game_short_name: str
    reply_markup: Optional[InlineKeyboardMarkup] = None
