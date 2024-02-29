# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List

from .photo_size import PhotoSize
from .sticker import Sticker
from .sticker_type import StickerType


@dataclass(frozen=True)
class StickerSet:
    """\
    Represents StickerSet object:
    https://core.telegram.org/bots/api#stickerset
    """

    name: str
    title: str
    sticker_type: StickerType
    is_animated: Optional[bool]
    is_video: Optional[bool]
    stickers: List[Sticker]
    thumbnail: Optional[PhotoSize]

    @classmethod
    def parse(cls, data: dict) -> Optional['StickerSet']:
        if data is None:
            return None

        try:
            sticker_type = StickerType(data['sticker_type'])
        except ValueError:
            sticker_type = StickerType.unknown

        return cls(
            data['name'],
            data['title'],
            sticker_type,
            data['is_animated'],
            data['is_video'],
            [Sticker.parse(s) for s in data['stickers']],
            PhotoSize.parse(data['thumbnail'])
        )
