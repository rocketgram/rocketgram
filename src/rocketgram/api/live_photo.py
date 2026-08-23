# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import List, Optional

from .photo_size import PhotoSize


@dataclass(frozen=True)
class LivePhoto:
    """\
    Represents LivePhoto object:
    https://core.telegram.org/bots/api#livephoto
    """

    photo: Optional[List[PhotoSize]]
    file_id: str
    file_unique_id: str
    width: int
    height: int
    duration: int
    mime_type: Optional[str]
    file_size: Optional[int]

    @classmethod
    def parse(cls, data: dict) -> Optional['LivePhoto']:
        if data is None:
            return None

        return cls(
            [PhotoSize.parse(d) for d in data['photo']] if 'photo' in data else None,
            data['file_id'],
            data['file_unique_id'],
            data['width'],
            data['height'],
            data['duration'],
            data.get('mime_type'),
            data.get('file_size'),
        )
