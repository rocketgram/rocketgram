# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional, List

from . import link_preview_options
from . import reply_parameters
from .message_entity import MessageEntity
from .parse_mode_type import ParseModeType
from .request import Request
from .utils import AnyKeyboard, MessageResultMixin


@dataclass(frozen=True)
class SendMessage(MessageResultMixin, Request):
    """\
    Represents SendMessage request object:
    https://core.telegram.org/bots/api#sendmessage
    """

    chat_id: Union[int, str]
    text: str
    message_thread_id: Optional[int] = None
    parse_mode: Optional[ParseModeType] = None
    entities: Optional[List[MessageEntity]] = None
    link_preview_options: Optional['link_preview_options.LinkPreviewOptions'] = None
    disable_notification: Optional[bool] = None
    protect_content: Optional[bool] = None
    reply_parameters: Optional['reply_parameters.ReplyParameters'] = None
    reply_markup: Optional[AnyKeyboard] = None
