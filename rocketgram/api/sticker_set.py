# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import List, Optional

from .photo_size import PhotoSize
from .sticker import Sticker


@dataclass(frozen=True)
class StickerSet:
    """\
    Represents StickerSet object:
    https://core.telegram.org/bots/api#stickerset
    """

    name: str
    title: str
    contains_masks: bool
    stickers: List[Sticker]
    thumb: Optional[PhotoSize]

    @classmethod
    def parse(cls, data: dict) -> Optional['StickerSet']:
        if data is None:
            return None

        stickers = [Sticker.parse(s) for s in data['stickers']]

        return cls(data['name'], data['title'], data['contains_masks'], stickers, PhotoSize.parse(data['thumb']))
