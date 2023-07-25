# Copyright (C) 2015-2023 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, Tuple

from .request import Request
from .. import api
from ..context import context


@dataclass(frozen=True)
class GetGameHighScores(Request):
    """\
    Represents GetGameHighScores request object:
    https://core.telegram.org/bots/api#getgamehighscores
    """

    user_id: int
    chat_id: Optional[int] = None
    message_id: Optional[int] = None
    inline_message_id: Optional[str] = None

    @staticmethod
    def parse_result(data) -> Tuple['api.GameHighScore', ...]:
        assert isinstance(data, list), "Should be dict."
        return tuple(api.GameHighScore.parse(r) for r in data)

    async def send(self) -> 'api.GameHighScore':
        res = await context.bot.send(self)
        return res.result
