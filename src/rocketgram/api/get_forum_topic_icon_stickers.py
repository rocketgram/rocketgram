# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import List

from .request import Request
from .sticker import Sticker
from .. import context


@dataclass(frozen=True)
class GetForumTopicIconStickers(Request):
    """\
    Represents GetForumTopicIconStickers request object:
    https://core.telegram.org/bots/api#getforumtopiciconstickers
    """

    def parse_result(self, data) -> List[Sticker]:
        assert isinstance(data, list), "Should be list."
        return [Sticker.parse(r) for r in data]

    async def send(self) -> List[Sticker]:
        res = await context.bot.send(self)
        return res.result
