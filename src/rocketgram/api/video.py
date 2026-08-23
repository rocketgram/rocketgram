# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List

from .photo_size import PhotoSize
from .video_quality import VideoQuality


@dataclass(frozen=True)
class Video:
    """\
    Represents Video object:
    https://core.telegram.org/bots/api#video
    """

    file_id: str
    file_unique_id: str
    width: int
    height: int
    duration: int
    thumbnail: Optional[PhotoSize]
    cover: Optional[List[PhotoSize]]
    start_timestamp: Optional[int]
    qualities: Optional[List[VideoQuality]]
    file_name: Optional[str]
    mime_type: Optional[str]
    file_size: Optional[int]

    @classmethod
    def parse(cls, data: dict) -> Optional['Video']:
        if data is None:
            return None

        return cls(
            data['file_id'],
            data['file_unique_id'],
            data['width'], data['height'],
            data['duration'],
            PhotoSize.parse(data.get('thumbnail')),
            [PhotoSize.parse(p) for p in data['cover']] if 'cover' in data else None,
            data.get('start_timestamp'),
            [VideoQuality.parse(q) for q in data['qualities']] if 'qualities' in data else None,
            data.get('file_name'),
            data.get('mime_type'),
            data.get('file_size')
        )
