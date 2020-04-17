# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass

from .request import Request
from .. import api


@dataclass(frozen=True)
class GetStickerSet(Request):
    """\
    Represents GetStickerSet request object:
    https://core.telegram.org/bots/api#getstickerset
    """

    method = "getStickerSet"

    name: str

    def parse_result(self, data) -> 'api.StickerSet':
        assert isinstance(data, dict), "Should be dict."
        return api.StickerSet.parse(data)

    async def send2(self) -> 'api.StickerSet':
        res = await self._send()
        return res.result
