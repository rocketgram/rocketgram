# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class VideoQuality:
    """\
    Represents VideoQuality object:
    https://core.telegram.org/bots/api#videoquality
    """

    file_id: str
    file_unique_id: str
    width: int
    height: int
    codec: str
    file_size: Optional[int]

    @classmethod
    def parse(cls, data: dict) -> Optional['VideoQuality']:
        if data is None:
            return None

        return cls(
            data['file_id'],
            data['file_unique_id'],
            data['width'],
            data['height'],
            data['codec'],
            data.get('file_size'),
        )
