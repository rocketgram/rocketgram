# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List

from .inline_query_result import InlineQueryResult
from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class AnswerInlineQuery(BoolResultMixin, Request):
    """\
    Represents AnswerInlineQuery request object:
    https://core.telegram.org/bots/api#answerinlinequery
    """

    inline_query_id: str
    results: List[InlineQueryResult]
    cache_time: Optional[int] = None
    is_personal: Optional[bool] = None
    next_offset: Optional[str] = None
    switch_pm_text: Optional[str] = None
    switch_pm_parameter: Optional[str] = None
