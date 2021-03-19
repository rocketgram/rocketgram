# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List

from .request import Request
from .shipping_option import ShippingOption
from .utils import BoolResultMixin


@dataclass(frozen=True)
class AnswerShippingQuery(BoolResultMixin, Request):
    """\
    Represents AnswerShippingQuery request object:
    https://core.telegram.org/bots/api#answershippingquery
    """

    shipping_query_id: str
    ok: bool
    shipping_options: Optional[List[ShippingOption]]
    error_message: Optional[str]
