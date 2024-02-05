# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Tuple

from .request import Request
from .sticker import Sticker
from ..context import context


@dataclass(frozen=True)
class GetCustomEmojiStickers(Request):
    """\
    Represents GetCustomEmojiStickers request object:
    https://core.telegram.org/bots/api#getcustomemojistickers
    """

    custom_emoji_ids: Tuple[str, ...]

    @staticmethod
    def parse_result(data) -> Tuple[Sticker, ...]:
        assert isinstance(data, list), "Should be list."
        return tuple(Sticker.parse(r) for r in data)

    async def send(self) -> Tuple[Sticker, ...]:
        res = await context.bot.send(self)
        return res.result
