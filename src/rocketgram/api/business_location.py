# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .location import Location


@dataclass(frozen=True)
class BusinessLocation:
    """\
    Represents BusinessLocation object:
    https://core.telegram.org/bots/api#businesslocation
    """

    address: str
    location: Optional[Location]

    @classmethod
    def parse(cls, data: dict) -> Optional['BusinessLocation']:
        if data is None:
            return None

        return cls(
            data['address'],
            Location.parse(data.get('location')),
        )
