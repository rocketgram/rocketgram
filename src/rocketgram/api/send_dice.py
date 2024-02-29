# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional

from . import reply_parameters
from .dice_type import DiceType
from .request import Request
from .utils import AnyKeyboard, MessageResultMixin


@dataclass(frozen=True)
class SendDice(MessageResultMixin, Request):
    """\
    Represents SendPoll request object:
    https://core.telegram.org/bots/api#senddice
    """

    chat_id: Union[int, str]
    message_thread_id: Optional[int] = None
    emoji: Optional[DiceType] = None
    disable_notification: Optional[bool] = None
    protect_content: Optional[bool] = None
    reply_parameters: Optional['reply_parameters.ReplyParameters'] = None
    reply_markup: Optional[AnyKeyboard] = None
