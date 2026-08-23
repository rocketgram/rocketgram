# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass

from .. import api
from ..context import context
from .inline_query_result import InlineQueryResult
from .request import Request


@dataclass(frozen=True)
class AnswerGuestQuery(Request):
    """\
    Represents AnswerGuestQuery request object:
    https://core.telegram.org/bots/api#answerguestquery
    """

    guest_query_id: str
    result: InlineQueryResult

    def parse_result(self, data) -> 'api.SentGuestMessage':
        assert isinstance(data, dict), "Should be dict."
        return api.SentGuestMessage.parse(data)

    async def send(self) -> 'api.SentGuestMessage':
        res = await context.bot.send(self)
        return res.result
