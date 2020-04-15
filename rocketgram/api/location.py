# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Location:
    """\
    Represents Location object:
    https://core.telegram.org/bots/api#location
    """

    longitude: float
    latitude: float

    @classmethod
    def parse(cls, data: dict) -> Optional['Location']:
        if data is None:
            return None

        return cls(data['longitude'], data['latitude'])
