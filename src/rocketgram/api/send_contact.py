# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional

from . import reply_parameters
from .request import Request
from .utils import AnyKeyboard, MessageResultMixin


@dataclass(frozen=True)
class SendContact(MessageResultMixin, Request):
    """\
    Represents SendContact request object:
    https://core.telegram.org/bots/api#sendcontact
    """

    chat_id: Union[int, str]
    phone_number: str
    first_name: str
    last_name: Optional[str] = None
    message_thread_id: Optional[int] = None
    vcard: Optional[str] = None
    disable_notification: Optional[bool] = None
    protect_content: Optional[bool] = None
    reply_parameters: Optional['reply_parameters.ReplyParameters'] = None
    reply_markup: Optional[AnyKeyboard] = None
