# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .. import api
from ..context import context
from .inline_query_result import InlineQueryResult
from .request import Request


@dataclass(frozen=True)
class SavePreparedInlineMessage(Request):
    """    Represents SavePreparedInlineMessage request object:
    https://core.telegram.org/bots/api#savepreparedinlinemessage
    """

    user_id: int
    result: InlineQueryResult
    allow_user_chats: Optional[bool] = None
    allow_bot_chats: Optional[bool] = None
    allow_group_chats: Optional[bool] = None
    allow_channel_chats: Optional[bool] = None

    def parse_result(self, data) -> 'api.PreparedInlineMessage':
        assert isinstance(data, dict), "Should be dict."
        return api.PreparedInlineMessage.parse(data)

    async def send(self) -> 'api.PreparedInlineMessage':
        res = await context.bot.send(self)
        return res.result
