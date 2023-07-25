# Copyright (C) 2015-2023 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass

from .request import Request
from .. import api
from ..context import context


@dataclass(frozen=True)
class GetMe(Request):
    """\
    Represents GetMe request object:
    https://core.telegram.org/bots/api#getme
    """

    @staticmethod
    def parse_result(data) -> 'api.User':
        assert isinstance(data, dict), "Should be dict."
        return api.User.parse(data)

    async def send(self) -> 'api.User':
        res = await context.bot.send(self)
        return res.result
