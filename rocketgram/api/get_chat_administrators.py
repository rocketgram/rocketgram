# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, List

from .request import Request
from .. import api
from ..context import context


@dataclass(frozen=True)
class GetChatAdministrators(Request):
    """\
    Represents GetChatAdministrators request object:
    https://core.telegram.org/bots/api#getchatadministrators
    """

    chat_id: Union[int, str]

    def parse_result(self, data) -> List['api.ChatMember']:
        assert isinstance(data, list), "Should be list."
        return [api.ChatMember.parse(r) for r in data]

    async def send(self) -> List['api.ChatMember']:
        res = await context.bot.send(self)
        return res.result
