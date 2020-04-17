# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .request import Request
from .. import api


@dataclass(frozen=True)
class GetUserProfilePhotos(Request):
    """\
    Represents GetUserProfilePhotos request object:
    https://core.telegram.org/bots/api#getuserprofilephotos
    """

    method = "getUserProfilePhotos"

    user_id: int
    offset: Optional[int] = None
    limit: Optional[int] = None

    def parse_result(self, data) -> 'api.UserProfilePhotos':
        assert isinstance(data, dict), "Should be dict."
        return api.UserProfilePhotos.parse(data)

    async def send2(self) -> 'api.UserProfilePhotos':
        res = await self._send()
        return res.result
