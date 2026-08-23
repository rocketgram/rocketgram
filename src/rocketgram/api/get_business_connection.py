# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass

from .. import api
from ..context import context
from .request import Request


@dataclass(frozen=True)
class GetBusinessConnection(Request):
    """    Represents GetBusinessConnection request object:
    https://core.telegram.org/bots/api#getbusinessconnection
    """

    business_connection_id: str

    def parse_result(self, data) -> 'api.BusinessConnection':
        assert isinstance(data, dict), "Should be dict."
        return api.BusinessConnection.parse(data)

    async def send(self) -> 'api.BusinessConnection':
        res = await context.bot.send(self)
        return res.result
