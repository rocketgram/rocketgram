# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional

from .request import Request
from .utils import AnyInlineKeyboard
from .. import api
from ..context import context


@dataclass(frozen=True)
class StopPoll(Request):
    """\
    Represents StopPoll request object:
    https://core.telegram.org/bots/api#stoppoll
    """

    chat_id: Union[int, str]
    message_id: int
    business_connection_id: Optional[str] = None
    reply_markup: Optional[AnyInlineKeyboard] = None

    def parse_result(self, data) -> 'api.Poll':
        assert isinstance(data, dict), "Should be dict."
        return api.Poll.parse(data)

    async def send(self) -> 'api.Poll':
        res = await context.bot.send(self)
        return res.result
