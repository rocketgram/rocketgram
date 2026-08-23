# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List

from .paid_media import PaidMedia


@dataclass(frozen=True)
class PaidMediaInfo:
    """\
    Represents PaidMediaInfo object:
    https://core.telegram.org/bots/api#paidmediainfo
    """

    star_count: int
    paid_media: List[PaidMedia]

    @classmethod
    def parse(cls, data: dict) -> Optional['PaidMediaInfo']:
        if data is None:
            return None

        return cls(
            data['star_count'],
            [PaidMedia.parse(p) for p in data['paid_media']]
        )

