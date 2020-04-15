# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional, List

from .poll_type import PollType
from .request import Request
from .utils import ALL_KEYBOARDS


@dataclass(frozen=True)
class SendPoll(Request):
    """\
    Represents SendPoll request object:
    https://core.telegram.org/bots/api#sendpoll
    """

    method = "sendPoll"

    chat_id: Union[int, str]
    question: str
    options: List[str]
    is_anonymous: Optional[bool] = None
    type: Optional['PollType'] = None
    allows_multiple_answers: Optional[bool] = None
    correct_option_id: Optional[int] = None
    is_closed: Optional[bool] = None
    disable_notification: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    reply_markup: Optional[ALL_KEYBOARDS] = None
