# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class AnswerPreCheckoutQuery(BoolResultMixin, Request):
    """\
    Represents AnswerPreCheckoutQuery request object:
    https://core.telegram.org/bots/api#answerprecheckoutquery
    """

    pre_checkout_query_id: str
    ok: bool
    error_message: Optional[str]
