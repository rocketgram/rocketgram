# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class SetBusinessAccountBio(BoolResultMixin, Request):
    """\
    Represents SetBusinessAccountBio request object:
    https://core.telegram.org/bots/api#setbusinessaccountbio
    """

    business_connection_id: str
    bio: Optional[str] = None
