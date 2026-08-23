# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .. import api
from ..context import context
from .request import Request


@dataclass(frozen=True)
class GetStarTransactions(Request):
    """    Represents GetStarTransactions request object:
    https://core.telegram.org/bots/api#getstartransactions
    """

    offset: Optional[int] = None
    limit: Optional[int] = None

    def parse_result(self, data) -> 'api.StarTransactions':
        assert isinstance(data, dict), "Should be dict."
        return api.StarTransactions.parse(data)

    async def send(self) -> 'api.StarTransactions':
        res = await context.bot.send(self)
        return res.result
