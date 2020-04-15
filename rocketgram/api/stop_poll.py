# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional

from .request import Request
from .utils import INLINE_KEYBOARDS


@dataclass(frozen=True)
class StopPoll(Request):
    """\
    Represents StopPoll request object:
    https://core.telegram.org/bots/api#stoppoll
    """

    method = "stopPoll"

    chat_id: Optional[Union[int, str]] = None
    message_id: Optional[int] = None
    reply_markup: Optional[INLINE_KEYBOARDS] = None
