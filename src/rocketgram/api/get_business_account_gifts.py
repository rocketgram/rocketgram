# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .. import api
from ..context import context
from .request import Request


@dataclass(frozen=True)
class GetBusinessAccountGifts(Request):
    """    Represents GetBusinessAccountGifts request object:
    https://core.telegram.org/bots/api#getbusinessaccountgifts
    """

    business_connection_id: str
    exclude_unsaved: Optional[bool] = None
    exclude_saved: Optional[bool] = None
    exclude_unlimited: Optional[bool] = None
    exclude_limited_upgradable: Optional[bool] = None
    exclude_limited_non_upgradable: Optional[bool] = None
    exclude_unique: Optional[bool] = None
    exclude_from_blockchain: Optional[bool] = None
    sort_by_price: Optional[bool] = None
    offset: Optional[str] = None
    limit: Optional[int] = None

    def parse_result(self, data) -> 'api.OwnedGifts':
        assert isinstance(data, dict), "Should be dict."
        return api.OwnedGifts.parse(data)

    async def send(self) -> 'api.OwnedGifts':
        res = await context.bot.send(self)
        return res.result
