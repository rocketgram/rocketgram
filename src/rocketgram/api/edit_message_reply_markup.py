# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional

from .request import Request
from .utils import AnyInlineKeyboard, MessageOrBoolResultMixin


@dataclass(frozen=True)
class EditMessageReplyMarkup(MessageOrBoolResultMixin, Request):
    """\
    Represents EditMessageReplyMarkup request object:
    https://core.telegram.org/bots/api#editmessagereplymarkup
    """

    chat_id: Optional[Union[int, str]] = None
    message_id: Optional[int] = None
    inline_message_id: Optional[str] = None
    reply_markup: Optional[AnyInlineKeyboard] = None
