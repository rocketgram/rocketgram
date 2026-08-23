# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Any, Optional

from .rich_text import RichText


@dataclass(frozen=True)
class RichBlockCaption:
    """\
    Represents RichBlockCaption object:
    https://core.telegram.org/bots/api#richblockcaption
    """

    text: Any
    credit: Optional[Any] = None

    @classmethod
    def parse(cls, data: dict) -> Optional['RichBlockCaption']:
        if data is None:
            return None

        return cls(RichText.parse(data['text']), RichText.parse(data.get('credit')))
