# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class SetBusinessAccountName(BoolResultMixin, Request):
    """\
    Represents SetBusinessAccountName request object:
    https://core.telegram.org/bots/api#setbusinessaccountname
    """

    business_connection_id: str
    first_name: str
    last_name: Optional[str] = None
