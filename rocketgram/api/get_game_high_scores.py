# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .request import Request


@dataclass(frozen=True)
class GetGameHighScores(Request):
    """\
    Represents GetGameHighScores request object:
    https://core.telegram.org/bots/api#getgamehighscores
    """

    method = "getGameHighScores"

    user_id: int
    chat_id: Optional[int] = None
    message_id: Optional[int] = None
    inline_message_id: Optional[str] = None
