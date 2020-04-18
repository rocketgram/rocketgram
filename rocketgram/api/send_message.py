# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional

from .parse_mode_type import ParseModeType
from .request import Request
from .utils import ALL_KEYBOARDS, MessageResultMixin


@dataclass(frozen=True)
class SendMessage(MessageResultMixin, Request):
    """\
    Represents SendMessage request object:
    https://core.telegram.org/bots/api#sendmessage
    """

    chat_id: Union[int, str]
    text: str
    parse_mode: Optional[ParseModeType] = None
    disable_web_page_preview: Optional[bool] = None
    disable_notification: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    reply_markup: Optional[ALL_KEYBOARDS] = None


