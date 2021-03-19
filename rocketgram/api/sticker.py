# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .mask_position import MaskPosition
from .photo_size import PhotoSize


@dataclass(frozen=True)
class Sticker:
    """\
    Represents Sticker object:
    https://core.telegram.org/bots/api#sticker
    """

    file_id: str
    file_unique_id: str
    width: int
    height: int
    is_animated: Optional[bool]
    thumb: Optional[PhotoSize]
    emoji: Optional[str]
    set_name: Optional[str]
    mask_position: Optional[MaskPosition]
    file_size: Optional[str]

    @classmethod
    def parse(cls, data: dict) -> Optional['Sticker']:
        if data is None:
            return None

        return cls(data['file_id'], data['file_unique_id'], data['width'], data['height'], data['is_animated'],
                   PhotoSize.parse(data.get('thumb')), data.get('emoji'), data.get('set_name'),
                   MaskPosition.parse(data.get('mask_position')), data.get('file_size'))
