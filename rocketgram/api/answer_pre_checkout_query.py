# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .request import Request


@dataclass(frozen=True)
class AnswerPreCheckoutQuery(Request):
    """\
    Represents AnswerPreCheckoutQuery request object:
    https://core.telegram.org/bots/api#answerprecheckoutquery
    """

    method = "answerPreCheckoutQuery"

    pre_checkout_query_id: str
    ok: bool
    error_message: Optional[str]
