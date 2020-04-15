# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .request import Request


@dataclass(frozen=True)
class AnswerCallbackQuery(Request):
    """\
    Represents AnswerCallbackQuery request object:
    https://core.telegram.org/bots/api#answercallbackquery
    """

    method = "answerCallbackQuery"

    callback_query_id: str
    text: Optional[str] = None
    show_alert: Optional[bool] = None
    url: Optional[str] = None
    cache_time: Optional[int] = None