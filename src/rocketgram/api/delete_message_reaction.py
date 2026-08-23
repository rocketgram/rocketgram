# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, Union

from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class DeleteMessageReaction(BoolResultMixin, Request):
    """\
    Represents DeleteMessageReaction request object:
    https://core.telegram.org/bots/api#deletemessagereaction
    """

    chat_id: Union[int, str]
    message_id: int
    user_id: Optional[int] = None
    actor_chat_id: Optional[int] = None
