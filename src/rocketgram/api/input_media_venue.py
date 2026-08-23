# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass, field
from typing import Optional

from .input_media import InputMedia


@dataclass(frozen=True)
class InputMediaVenue(InputMedia):
    """\
    Represents InputMediaVenue object:
    https://core.telegram.org/bots/api#inputmediavenue
    """

    type: str = field(init=False, default='venue')

    latitude: float
    longitude: float
    title: str
    address: str
    foursquare_id: Optional[str] = None
    foursquare_type: Optional[str] = None
    google_place_id: Optional[str] = None
    google_place_type: Optional[str] = None
