# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from datetime import datetime
from typing import Union, Optional, List

from . import reply_parameters
from .message_entity import MessageEntity
from .poll_type import PollType
from .request import Request
from .utils import AnyKeyboard, MessageResultMixin
from .. import api


@dataclass(frozen=True)
class SendPoll(MessageResultMixin, Request):
    """\
    Represents SendPoll request object:
    https://core.telegram.org/bots/api#sendpoll
    """

    chat_id: Union[int, str]
    question: str
    options: List[str]
    message_thread_id: Optional[int] = None
    is_anonymous: Optional[bool] = None
    type: Optional['PollType'] = None
    allows_multiple_answers: Optional[bool] = None
    correct_option_id: Optional[int] = None
    explanation: Optional[str] = None
    explanation_parse_mode: Optional['api.ParseModeType'] = None
    explanation_entities: Optional[List[MessageEntity]] = None
    open_period: Optional[int] = None
    close_date: Optional[datetime] = None
    is_closed: Optional[bool] = None
    disable_notification: Optional[bool] = None
    protect_content: Optional[bool] = None
    reply_parameters: Optional['reply_parameters.ReplyParameters'] = None
    reply_markup: Optional[AnyKeyboard] = None
