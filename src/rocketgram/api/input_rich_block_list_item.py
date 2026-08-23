# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, List, Optional

if TYPE_CHECKING:
    from .input_rich_block import InputRichBlock


@dataclass(frozen=True)
class InputRichBlockListItem:
    """\
    Represents InputRichBlockListItem object:
    https://core.telegram.org/bots/api#inputrichblocklistitem
    """

    blocks: List[InputRichBlock]
    has_checkbox: Optional[bool] = None
    is_checked: Optional[bool] = None
    value: Optional[int] = None
    type: Optional[str] = None
