# Copyright (C) 2015-2023 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from datetime import datetime
from typing import Union, Optional, Tuple

from .message_entity import MessageEntity
from .parse_mode_type import ParseModeType
from .poll_type import PollType
from .request import Request
from .utils import AnyKeyboard, MessageResultMixin


@dataclass(frozen=True)
class SendPoll(MessageResultMixin, Request):
    """\
    Represents SendPoll request object:
    https://core.telegram.org/bots/api#sendpoll
    """

    chat_id: Union[int, str]
    question: str
    options: Tuple[str, ...]
    message_thread_id: Optional[int] = None
    is_anonymous: Optional[bool] = None
    type: Optional[PollType] = None
    allows_multiple_answers: Optional[bool] = None
    correct_option_id: Optional[int] = None
    explanation: Optional[str] = None
    explanation_parse_mode: Optional[ParseModeType] = None
    explanation_entities: Optional[Tuple[MessageEntity, ...]] = None
    open_period: Optional[int] = None
    close_date: Optional[datetime] = None
    is_closed: Optional[bool] = None
    disable_notification: Optional[bool] = None
    protect_content: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    allow_sending_without_reply: Optional[bool] = None
    reply_markup: Optional[AnyKeyboard] = None
