# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List

from .request import Request
from .. import api


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

    def parse_result(self, data) -> List['api.GameHighScore']:
        assert isinstance(data, list), "Should be dict."
        return [api.GameHighScore.parse(r) for r in data]

    async def send2(self) -> 'api.GameHighScore':
        res = await self._send()
        return res.result
