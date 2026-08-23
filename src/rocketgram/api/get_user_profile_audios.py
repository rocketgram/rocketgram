# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .. import api
from ..context import context
from .request import Request


@dataclass(frozen=True)
class GetUserProfileAudios(Request):
    """    Represents GetUserProfileAudios request object:
    https://core.telegram.org/bots/api#getuserprofileaudios
    """

    user_id: int
    offset: Optional[int] = None
    limit: Optional[int] = None

    def parse_result(self, data) -> 'api.UserProfileAudios':
        assert isinstance(data, dict), "Should be dict."
        return api.UserProfileAudios.parse(data)

    async def send(self) -> 'api.UserProfileAudios':
        res = await context.bot.send(self)
        return res.result
