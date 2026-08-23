# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, Union

from .inline_keyboard_markup import InlineKeyboardMarkup
from .input_checklist import InputChecklist
from .reply_parameters import ReplyParameters
from .request import Request
from .utils import MessageResultMixin


@dataclass(frozen=True)
class SendChecklist(MessageResultMixin, Request):
    """\
    Represents SendChecklist request object:
    https://core.telegram.org/bots/api#sendchecklist
    """

    business_connection_id: str
    chat_id: Union[int, str]
    checklist: InputChecklist
    disable_notification: Optional[bool] = None
    protect_content: Optional[bool] = None
    message_effect_id: Optional[str] = None
    reply_parameters: Optional[ReplyParameters] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
