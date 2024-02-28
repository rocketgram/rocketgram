# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass

from .inline_query_result import InlineQueryResult
from .request import Request
from .sent_web_app_message import SentWebAppMessage
from .utils import BoolResultMixin
from ..context import context


@dataclass(frozen=True)
class AnswerWebAppQuery(BoolResultMixin, Request):
    """\
    Represents AnswerWebAppQuery request object:
    https://core.telegram.org/bots/api#answerwebappquery
    """

    web_app_query_id: str
    results: InlineQueryResult

    def parse_result(self, data) -> SentWebAppMessage:
        assert isinstance(data, dict), "Should be dict."

        return SentWebAppMessage.parse(data)

    async def send(self) -> SentWebAppMessage:
        res = await context.bot.send(self)

        return res.result
