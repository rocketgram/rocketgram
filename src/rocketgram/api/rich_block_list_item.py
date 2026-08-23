# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, List, Optional

if TYPE_CHECKING:
    from .rich_block import RichBlock


@dataclass(frozen=True)
class RichBlockListItem:
    """\
    Represents RichBlockListItem object:
    https://core.telegram.org/bots/api#richblocklistitem
    """

    label: str
    blocks: List[RichBlock]
    has_checkbox: Optional[bool] = None
    is_checked: Optional[bool] = None
    value: Optional[int] = None
    type: Optional[str] = None

    @classmethod
    def parse(cls, data: dict) -> Optional['RichBlockListItem']:
        if data is None:
            return None

        from .rich_block import RichBlock

        return cls(
            data['label'],
            [RichBlock.parse(d) for d in data['blocks']],
            data.get('has_checkbox'),
            data.get('is_checked'),
            data.get('value'),
            data.get('type'),
        )
