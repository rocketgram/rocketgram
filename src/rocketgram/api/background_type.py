# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from . import document as document_mod
from .background_fill import BackgroundFill
from .background_type_type import BackgroundTypeType


@dataclass(frozen=True)
class BackgroundType:
    """    Represents BackgroundType, BackgroundTypeFill, BackgroundTypeWallpaper,
    BackgroundTypePattern, BackgroundTypeChatTheme objects:
    https://core.telegram.org/bots/api#backgroundtype
    """

    type: BackgroundTypeType
    fill: Optional[BackgroundFill]
    dark_theme_dimming: Optional[int]
    document: Optional['document_mod.Document']
    is_blurred: Optional[bool]
    is_moving: Optional[bool]
    intensity: Optional[int]
    is_inverted: Optional[bool]
    theme_name: Optional[str]

    @classmethod
    def parse(cls, data: dict) -> Optional['BackgroundType']:
        if data is None:
            return None

        try:
            type_ = BackgroundTypeType(data['type'])
        except ValueError:
            type_ = BackgroundTypeType.unknown

        return cls(
            type_,
            BackgroundFill.parse(data.get('fill')),
            data.get('dark_theme_dimming'),
            document_mod.Document.parse(data.get('document')),
            data.get('is_blurred'),
            data.get('is_moving'),
            data.get('intensity'),
            data.get('is_inverted'),
            data.get('theme_name'),
        )
