# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, Union

from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class SetChatMemberTag(BoolResultMixin, Request):
    """\
    Represents SetChatMemberTag request object:
    https://core.telegram.org/bots/api#setchatmembertag
    """

    chat_id: Union[int, str]
    user_id: int
    tag: Optional[str] = None
