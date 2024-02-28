# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .bot_short_description import BotShortDescription
from .request import Request
from ..context import context


@dataclass(frozen=True)
class GetMyShortDescription(Request):
    """\
    Represents GetMyShortDescription request object:
    https://core.telegram.org/bots/api#getmyshortdescription
    """

    language_code: Optional[str] = None

    def parse_result(self, data) -> BotShortDescription:
        assert isinstance(data, dict), "Should be dict."

        return BotShortDescription.parse(data)

    async def send(self) -> BotShortDescription:
        res = await context.bot.send(self)

        return res.result
