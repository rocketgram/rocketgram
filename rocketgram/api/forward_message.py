# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional

from .request import Request


@dataclass(frozen=True)
class ForwardMessage(Request):
    """\
    Represents ForwardMessage request object:
    https://core.telegram.org/bots/api#forwardmessage
    """

    method = "forwardMessage"

    chat_id: Union[int, str]
    from_chat_id: Union[int, str]
    message_id: int
    disable_notification: Optional[bool] = None
