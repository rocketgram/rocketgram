# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .request import Request


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
