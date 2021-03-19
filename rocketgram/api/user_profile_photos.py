# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import List, Optional

from .photo_size import PhotoSize


@dataclass(frozen=True)
class UserProfilePhotos:
    """\
    Represents UserProfilePhotos object:
    https://core.telegram.org/bots/api#userprofilephotos
    """

    total_count: int
    photos: List[List[PhotoSize]]

    @classmethod
    def parse(cls, data: dict) -> Optional['UserProfilePhotos']:
        if data is None:
            return None

        photos = [[PhotoSize.parse(i) for i in p] for p in data['photos']]

        return cls(data['total_count'], photos)
