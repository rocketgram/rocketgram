# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass, field
from typing import Optional, Union

from .input_file import InputFile
from .input_media import InputMedia


@dataclass(frozen=True)
class InputMediaSticker(InputMedia):
    """\
    Represents InputMediaSticker object:
    https://core.telegram.org/bots/api#inputmediasticker
    """

    type: str = field(init=False, default='sticker')

    media: Union[InputFile, str]
    emoji: Optional[str] = None
