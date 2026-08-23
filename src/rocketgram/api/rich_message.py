# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import List, Optional

from .rich_block import RichBlock


@dataclass(frozen=True)
class RichMessage:
    """\
    Represents RichMessage object:
    https://core.telegram.org/bots/api#richmessage
    """

    blocks: List[RichBlock]
    is_rtl: Optional[bool]

    @classmethod
    def parse(cls, data: dict) -> Optional['RichMessage']:
        if data is None:
            return None

        return cls(
            [RichBlock.parse(d) for d in data['blocks']],
            data.get('is_rtl'),
        )
