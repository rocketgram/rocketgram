# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .inline_keyboard_markup import InlineKeyboardMarkup
from .input_checklist import InputChecklist
from .request import Request
from .utils import MessageResultMixin


@dataclass(frozen=True)
class EditMessageChecklist(MessageResultMixin, Request):
    """    Represents EditMessageChecklist request object:
    https://core.telegram.org/bots/api#editmessagechecklist
    """

    business_connection_id: str
    chat_id: int
    message_id: int
    checklist: InputChecklist
    reply_markup: Optional[InlineKeyboardMarkup] = None
