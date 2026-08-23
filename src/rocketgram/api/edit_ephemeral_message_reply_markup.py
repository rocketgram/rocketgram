# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, Union

from .request import Request
from .utils import AnyInlineKeyboard, BoolResultMixin


@dataclass(frozen=True)
class EditEphemeralMessageReplyMarkup(BoolResultMixin, Request):
    """\
    Represents EditEphemeralMessageReplyMarkup request object:
    https://core.telegram.org/bots/api#editephemeralmessagereplymarkup
    """

    chat_id: Union[int, str]
    receiver_user_id: int
    ephemeral_message_id: int
    reply_markup: Optional[AnyInlineKeyboard] = None
