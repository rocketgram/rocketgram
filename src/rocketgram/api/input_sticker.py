# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List, Union

from .input_file import InputFile
from .mask_position import MaskPosition
from .sticker_format import StickerFormat


@dataclass(frozen=True)
class InputSticker:
    """\
    Represents InputSticker object:
    https://core.telegram.org/bots/api#inputsticker
    """

    sticker: Union[InputFile, str]
    format: StickerFormat
    emoji_list: List[str]
    mask_position: Optional[MaskPosition] = None
    keywords: Optional[List[str]] = None
