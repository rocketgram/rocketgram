# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union

from .request import Request
from .. import api


@dataclass(frozen=True)
class GetChat(Request):
    """\
    Represents GetChat request object:
    https://core.telegram.org/bots/api#getchat
    """

    method = "getChat"

    chat_id: Union[int, str]

    def parse_result(self, data) -> 'api.Chat':
        assert isinstance(data, dict), "Should be dict."
        return api.Chat.parse(data)

    async def send2(self) -> 'api.Chat':
        res = await self._send()
        return res.result
