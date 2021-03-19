# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .location import Location


@dataclass(frozen=True)
class Venue:
    """\
    Represents Venue object:
    https://core.telegram.org/bots/api#venue
    """

    location: Location
    title: str
    address: str
    foursquare_id: Optional[str]
    foursquare_type: Optional[str]
    google_place_id: Optional[str]
    google_place_type: Optional[str]

    @classmethod
    def parse(cls, data: dict) -> Optional['Venue']:
        if data is None:
            return None

        return cls(Location.parse(data['location']), data['title'], data['address'],
                   data.get('foursquare_id'), data.get('foursquare_type'), data.get('google_place_id'),
                   data.get('google_place_type'))
