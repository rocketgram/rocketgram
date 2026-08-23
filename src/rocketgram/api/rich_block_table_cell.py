# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Any, Optional

from .rich_text import RichText


@dataclass(frozen=True)
class RichBlockTableCell:
    """\
    Represents RichBlockTableCell object:
    https://core.telegram.org/bots/api#richblocktablecell
    """

    align: str
    valign: str
    text: Optional[Any] = None
    is_header: Optional[bool] = None
    colspan: Optional[int] = None
    rowspan: Optional[int] = None

    @classmethod
    def parse(cls, data: dict) -> Optional['RichBlockTableCell']:
        if data is None:
            return None

        return cls(
            data['align'],
            data['valign'],
            RichText.parse(data.get('text')),
            data.get('is_header'),
            data.get('colspan'),
            data.get('rowspan'),
        )
