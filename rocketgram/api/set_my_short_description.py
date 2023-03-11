# Copyright (C) 2015-2022 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class SetMyShortDescription(BoolResultMixin, Request):
    """\
    Represents SetMyShortDescription request object:
    https://core.telegram.org/bots/api#setmyshortdescription
    """

    short_description: Optional[str] = None
    language_code: Optional[str] = None
