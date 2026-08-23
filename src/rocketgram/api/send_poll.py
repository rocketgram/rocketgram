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
from .input_poll_media import InputPollMedia
from .. import api


@dataclass(frozen=True)
class SendPoll(MessageResultMixin, Request):
    """\
    Represents SendPoll request object:
    https://core.telegram.org/bots/api#sendpoll
    """

    chat_id: Union[int, str]
    question: str
    options: list
    business_connection_id: Optional[str] = None
    message_thread_id: Optional[int] = None
    question_parse_mode: Optional[str] = None
    question_entities: Optional[List[MessageEntity]] = None
    is_anonymous: Optional[bool] = None
    type: Optional['PollType'] = None
    allows_multiple_answers: Optional[bool] = None
    explanation: Optional[str] = None
    explanation_parse_mode: Optional['api.ParseModeType'] = None
    explanation_entities: Optional[List[MessageEntity]] = None
    media: Optional[InputPollMedia] = None
    explanation_media: Optional[InputPollMedia] = None
    members_only: Optional[bool] = None
    country_codes: Optional[List[str]] = None
    allows_revoting: Optional[bool] = None
    shuffle_options: Optional[bool] = None
    allow_adding_options: Optional[bool] = None
    hide_results_until_closes: Optional[bool] = None
    correct_option_ids: Optional[List[int]] = None
    description: Optional[str] = None
    description_parse_mode: Optional['api.ParseModeType'] = None
    description_entities: Optional[List[MessageEntity]] = None
    open_period: Optional[int] = None
    close_date: Optional[datetime] = None
    is_closed: Optional[bool] = None
    disable_notification: Optional[bool] = None
    protect_content: Optional[bool] = None
    message_effect_id: Optional[str] = None
    allow_paid_broadcast: Optional[bool] = None
    reply_parameters: Optional['reply_parameters.ReplyParameters'] = None
    reply_markup: Optional[AnyKeyboard] = None
