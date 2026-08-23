# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import List, Optional

from .animation import Animation
from .audio import Audio
from .document import Document
from .link import Link
from .live_photo import LivePhoto
from .location import Location
from .photo_size import PhotoSize
from .sticker import Sticker
from .venue import Venue
from .video import Video


@dataclass(frozen=True)
class PollMedia:
    """\
    Represents PollMedia object:
    https://core.telegram.org/bots/api#pollmedia
    """

    animation: Optional[Animation]
    audio: Optional[Audio]
    document: Optional[Document]
    link: Optional[Link]
    live_photo: Optional[LivePhoto]
    location: Optional[Location]
    photo: Optional[List[PhotoSize]]
    sticker: Optional[Sticker]
    venue: Optional[Venue]
    video: Optional[Video]

    @classmethod
    def parse(cls, data: dict) -> Optional['PollMedia']:
        if data is None:
            return None

        return cls(
            Animation.parse(data.get('animation')),
            Audio.parse(data.get('audio')),
            Document.parse(data.get('document')),
            Link.parse(data.get('link')),
            LivePhoto.parse(data.get('live_photo')),
            Location.parse(data.get('location')),
            [PhotoSize.parse(d) for d in data['photo']] if 'photo' in data else None,
            Sticker.parse(data.get('sticker')),
            Venue.parse(data.get('venue')),
            Video.parse(data.get('video')),
        )
