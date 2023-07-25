# Copyright (C) 2015-2023 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, Union, Tuple

from .input_file import InputFile
from .mask_position import MaskPosition


@dataclass(frozen=True)
class InputSticker:
    """\
    Represents InputSticker object:
    https://core.telegram.org/bots/api#inputsticker
    """

    sticker: Union[InputFile, str]
    emoji_list: Tuple[str, ...]
    mask_position: Optional[MaskPosition] = None
    keywords: Optional[Tuple[str, ...]] = None
