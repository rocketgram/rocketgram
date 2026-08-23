# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, Union

from . import reply_parameters
from .request import Request
from .utils import AnyInlineKeyboard, MessageResultMixin


@dataclass(frozen=True)
class SendGame(MessageResultMixin, Request):
    """\
    Represents SendGame request object:
    https://core.telegram.org/bots/api#sendgame
    """

    chat_id: Union[int, str]
    game_short_name: str
    business_connection_id: Optional[str] = None
    message_thread_id: Optional[int] = None
    disable_notification: Optional[bool] = None
    protect_content: Optional[bool] = None
    allow_paid_broadcast: Optional[bool] = None
    message_effect_id: Optional[str] = None
    reply_parameters: Optional[reply_parameters.ReplyParameters] = None
    reply_markup: Optional[AnyInlineKeyboard] = None
