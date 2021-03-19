# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .request import Request
from .. import api
from ..context import context


@dataclass(frozen=True)
class GetUserProfilePhotos(Request):
    """\
    Represents GetUserProfilePhotos request object:
    https://core.telegram.org/bots/api#getuserprofilephotos
    """

    user_id: int
    offset: Optional[int] = None
    limit: Optional[int] = None

    def parse_result(self, data) -> 'api.UserProfilePhotos':
        assert isinstance(data, dict), "Should be dict."
        return api.UserProfilePhotos.parse(data)

    async def send(self) -> 'api.UserProfilePhotos':
        res = await context.bot.send(self)
        return res.result
