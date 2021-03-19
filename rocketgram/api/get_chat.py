# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union

from .request import Request
from .. import api
from ..context import context


@dataclass(frozen=True)
class GetChat(Request):
    """\
    Represents GetChat request object:
    https://core.telegram.org/bots/api#getchat
    """

    chat_id: Union[int, str]

    def parse_result(self, data) -> 'api.Chat':
        assert isinstance(data, dict), "Should be dict."
        return api.Chat.parse(data)

    async def send(self) -> 'api.Chat':
        res = await context.bot.send(self)
        return res.result
