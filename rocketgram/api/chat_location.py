# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Dict, Optional

from .location import Location


@dataclass(frozen=True)
class ChatLocation:
    """\
    Represents ChatPhoto object:
    https://core.telegram.org/bots/api#chatlocation
    """

    location: Location
    address: str

    @classmethod
    def parse(cls, data: Optional[Dict]) -> Optional['ChatLocation']:
        if data is None:
            return None

        return cls(Location.parse(data['location']), data['address'])
