# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import List, Optional

from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class SetManagedBotAccessSettings(BoolResultMixin, Request):
    """\
    Represents SetManagedBotAccessSettings request object:
    https://core.telegram.org/bots/api#setmanagedbotaccesssettings
    """

    user_id: int
    is_access_restricted: bool
    added_user_ids: Optional[List[int]] = None
