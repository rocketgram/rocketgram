# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import List

from .. import api
from ..context import context
from .request import Request


@dataclass(frozen=True)
class GetUserPersonalChatMessages(Request):
    """\
    Represents GetUserPersonalChatMessages request object:
    https://core.telegram.org/bots/api#getuserpersonalchatmessages
    """

    user_id: int
    limit: int

    def parse_result(self, data) -> List['api.Message']:
        assert isinstance(data, list), "Should be list."
        return [api.Message.parse(d) for d in data]

    async def send(self) -> List['api.Message']:
        res = await context.bot.send(self)
        return res.result
