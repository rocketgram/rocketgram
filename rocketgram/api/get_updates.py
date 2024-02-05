# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, Tuple

from .request import Request
from .update_type import UpdateType
from .. import api
from ..context import context


@dataclass(frozen=True)
class GetUpdates(Request):
    """\
    Represents GetUpdates request object:
    https://core.telegram.org/bots/api#getupdates
    """

    offset: Optional[int] = None
    limit: Optional[int] = None
    timeout: Optional[int] = None
    allowed_updates: Optional[Tuple[UpdateType, ...]] = None

    @staticmethod
    def parse_result(data) -> Tuple['api.Update', ...]:
        assert isinstance(data, list), "Should be list."
        return tuple(api.Update.parse(r) for r in data)

    async def send(self) -> Tuple['api.Update', ...]:
        res = await context.bot.send(self)
        return res.result
