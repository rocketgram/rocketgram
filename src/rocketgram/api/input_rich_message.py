# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import List, Optional

from .input_rich_block import InputRichBlock
from .input_rich_message_media import InputRichMessageMedia


@dataclass(frozen=True)
class InputRichMessage:
    """\
    Represents InputRichMessage object:
    https://core.telegram.org/bots/api#inputrichmessage
    """

    blocks: Optional[List[InputRichBlock]] = None
    html: Optional[str] = None
    markdown: Optional[str] = None
    media: Optional[List[InputRichMessageMedia]] = None
    is_rtl: Optional[bool] = None
    skip_entity_detection: Optional[bool] = None
