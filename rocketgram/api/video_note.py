# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .photo_size import PhotoSize


@dataclass(frozen=True)
class VideoNote:
    """\
    Represents VideoNote object:
    https://core.telegram.org/bots/api#videonote
    """

    file_id: str
    file_unique_id: str
    length: int
    duration: int
    thumb: Optional[PhotoSize]
    file_size: Optional[int]

    @classmethod
    def parse(cls, data: dict) -> Optional['VideoNote']:
        if data is None:
            return None

        return cls(data['file_id'], data['file_unique_id'], data['length'], data['duration'],
                   PhotoSize.parse(data.get('thumb')), data.get('file_size'))
