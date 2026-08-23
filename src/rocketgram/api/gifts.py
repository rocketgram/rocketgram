# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List

from .gift import Gift


@dataclass(frozen=True)
class Gifts:
    """\
    Represents Gifts object:
    https://core.telegram.org/bots/api#gifts
    """

    gifts: List[Gift]

    @classmethod
    def parse(cls, data: dict) -> Optional['Gifts']:
        if data is None:
            return None

        return cls([Gift.parse(g) for g in data['gifts']])

