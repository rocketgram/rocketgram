# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List

from . import link_preview_options
from .input_message_content import InputMessageContent
from .message_entity import MessageEntity
from .parse_mode_type import ParseModeType


@dataclass(frozen=True)
class InputTextMessageContent(InputMessageContent):
    """\
    Represents InputTextMessageContent object:
    https://core.telegram.org/bots/api#inputtextmessagecontent
    """

    message_text: str
    parse_mode: Optional[ParseModeType] = None
    entities: Optional[List[MessageEntity]] = None
    link_preview_options: Optional['link_preview_options.LinkPreviewOptions'] = None
