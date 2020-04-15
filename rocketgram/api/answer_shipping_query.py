# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List

from .request import Request
from .shipping_option import ShippingOption


@dataclass(frozen=True)
class AnswerShippingQuery(Request):
    """\
    Represents AnswerShippingQuery request object:
    https://core.telegram.org/bots/api#answershippingquery
    """

    method = "answerShippingQuery"

    shipping_query_id: str
    ok: bool
    shipping_options: Optional[List[ShippingOption]]
    error_message: Optional[str]
