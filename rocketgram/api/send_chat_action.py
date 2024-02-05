# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional

from .chat_action_type import ChatActionType
from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class SendChatAction(BoolResultMixin, Request):
    """\
    Represents SendChatAction request object:
    https://core.telegram.org/bots/api#sendchataction
    """

    chat_id: Union[int, str]
    action: ChatActionType
    message_thread_id: Optional[int] = None
