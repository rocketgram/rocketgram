# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .file import File
from .mask_position import MaskPosition
from .photo_size import PhotoSize
from .sticker_type import StickerType


@dataclass(frozen=True)
class Sticker:
    """\
    Represents Sticker object:
    https://core.telegram.org/bots/api#sticker
    """

    file_id: str
    file_unique_id: str
    type: StickerType
    width: int
    height: int
    is_animated: Optional[bool]
    is_video: Optional[bool]
    thumbnail: Optional[PhotoSize]
    emoji: Optional[str]
    set_name: Optional[str]
    premium_animation: Optional[File]
    mask_position: Optional[MaskPosition]
    custom_emoji_id: Optional[str]
    needs_repainting: Optional[bool]
    file_size: Optional[str]

    @classmethod
    def parse(cls, data: dict) -> Optional['Sticker']:
        if data is None:
            return None

        try:
            sticker_type = StickerType(data['type'])
        except ValueError:
            sticker_type = StickerType.unknown

        return cls(
            data['file_id'],
            data['file_unique_id'],
            sticker_type,
            data['width'],
            data['height'],
            data['is_animated'],
            data['is_video'],
            PhotoSize.parse(data.get('thumbnail')),
            data.get('emoji'),
            data.get('set_name'),
            File.parse(data.get('premium_animation')),
            MaskPosition.parse(data.get('mask_position')),
            data.get('custom_emoji_id'),
            data.get('needs_repainting'),
            data.get('file_size')
        )
