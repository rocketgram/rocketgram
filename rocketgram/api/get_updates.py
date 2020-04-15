# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List

from .request import Request
from .update_type import UpdateType


@dataclass(frozen=True)
class GetUpdates(Request):
    """\
    Represents GetUpdates request object:
    https://core.telegram.org/bots/api#getupdates
    """

    method = "getUpdates"

    offset: Optional[int] = None
    limit: Optional[int] = None
    timeout: Optional[int] = None
    allowed_updates: Optional[List[UpdateType]] = None
