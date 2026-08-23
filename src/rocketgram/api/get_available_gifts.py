# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass

from .. import api
from ..context import context
from .request import Request


@dataclass(frozen=True)
class GetAvailableGifts(Request):
    """    Represents GetAvailableGifts request object:
    https://core.telegram.org/bots/api#getavailablegifts
    """

    def parse_result(self, data) -> 'api.Gifts':
        assert isinstance(data, dict), "Should be dict."
        return api.Gifts.parse(data)

    async def send(self) -> 'api.Gifts':
        res = await context.bot.send(self)
        return res.result
