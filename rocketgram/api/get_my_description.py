# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .bot_description import BotDescription
from .request import Request
from ..context import context


@dataclass(frozen=True)
class GetMyDescription(Request):
    """\
    Represents GetMyDescription request object:
    https://core.telegram.org/bots/api#getmydescription
    """

    language_code: Optional[str] = None

    def parse_result(self, data) -> BotDescription:
        assert isinstance(data, dict), "Should be dict."

        return BotDescription.parse(data)

    async def send(self) -> BotDescription:
        res = await context.bot.send(self)

        return res.result
