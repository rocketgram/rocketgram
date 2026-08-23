# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass

from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class AnswerChatJoinRequestQuery(BoolResultMixin, Request):
    """\
    Represents AnswerChatJoinRequestQuery request object:
    https://core.telegram.org/bots/api#answerchatjoinrequestquery
    """

    chat_join_request_query_id: str
    result: str
