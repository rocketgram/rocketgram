# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List

from .paid_media_type import PaidMediaType
from .photo_size import PhotoSize
from .video import Video


@dataclass(frozen=True)
class PaidMedia:
    """\
    Represents PaidMedia, PaidMediaPreview, PaidMediaPhoto, PaidMediaVideo objects:
    https://core.telegram.org/bots/api#paidmedia
    """

    type: PaidMediaType
    width: Optional[int]
    height: Optional[int]
    duration: Optional[int]
    photo: Optional[List[PhotoSize]]
    video: Optional[Video]

    @classmethod
    def parse(cls, data: dict) -> Optional['PaidMedia']:
        if data is None:
            return None

        try:
            paid_media_type = PaidMediaType(data['type'])
        except ValueError:
            paid_media_type = PaidMediaType.unknown

        return cls(
            paid_media_type,
            data.get('width'),
            data.get('height'),
            data.get('duration'),
            [PhotoSize.parse(p) for p in data['photo']] if 'photo' in data else None,
            Video.parse(data.get('video'))
        )

