# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional

from .request import Request
from .utils import MessageResultMixin


@dataclass(frozen=True)
class ForwardMessage(MessageResultMixin, Request):
    """\
    Represents ForwardMessage request object:
    https://core.telegram.org/bots/api#forwardmessage
    """

    chat_id: Union[int, str]
    from_chat_id: Union[int, str]
    message_id: int
    disable_notification: Optional[bool] = None
