# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass

from .. import api
from ..context import context
from .request import Request


@dataclass(frozen=True)
class GetManagedBotAccessSettings(Request):
    """\
    Represents GetManagedBotAccessSettings request object:
    https://core.telegram.org/bots/api#getmanagedbotaccesssettings
    """

    user_id: int

    def parse_result(self, data) -> 'api.BotAccessSettings':
        assert isinstance(data, dict), "Should be dict."
        return api.BotAccessSettings.parse(data)

    async def send(self) -> 'api.BotAccessSettings':
        res = await context.bot.send(self)
        return res.result
