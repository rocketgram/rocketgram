# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class SetGameScore(BoolResultMixin, Request):
    """\
    Represents SetGameScore request object:
    https://core.telegram.org/bots/api#setgamescore
    """

    user_id: int
    score: int
    force: Optional[bool] = None
    disable_edit_message: Optional[bool] = None
    chat_id: Optional[int] = None
    message_id: Optional[int] = None
    inline_message_id: Optional[str] = None
