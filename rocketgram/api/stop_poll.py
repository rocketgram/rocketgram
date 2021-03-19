# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional

from .request import Request
from .utils import INLINE_KEYBOARDS
from .. import api
from ..context import context


@dataclass(frozen=True)
class StopPoll(Request):
    """\
    Represents StopPoll request object:
    https://core.telegram.org/bots/api#stoppoll
    """

    chat_id: Optional[Union[int, str]] = None
    message_id: Optional[int] = None
    reply_markup: Optional[INLINE_KEYBOARDS] = None

    def parse_result(self, data) -> 'api.Poll':
        assert isinstance(data, dict), "Should be dict."
        return api.Poll.parse(data)

    async def send(self) -> 'api.Poll':
        res = await context.bot.send(self)
        return res.result
