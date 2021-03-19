# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .request import Request
from .utils import INLINE_KEYBOARDS, MessageResultMixin


@dataclass(frozen=True)
class SendGame(MessageResultMixin, Request):
    """\
    Represents SendGame request object:
    https://core.telegram.org/bots/api#sendgame
    """

    chat_id: int
    game_short_name: str
    disable_notification: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    allow_sending_without_reply: Optional[bool] = None
    reply_markup: Optional[INLINE_KEYBOARDS] = None
