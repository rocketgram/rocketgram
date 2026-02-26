# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class SetBusinessAccountUsername(BoolResultMixin, Request):
    """\
    Represents SetBusinessAccountUsername request object:
    https://core.telegram.org/bots/api#setbusinessaccountusername
    """

    business_connection_id: str
    username: Optional[str] = None
