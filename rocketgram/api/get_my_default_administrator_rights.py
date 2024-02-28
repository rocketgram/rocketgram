# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .chat_administrator_rights import ChatAdministratorRights
from .request import Request
from ..context import context


@dataclass(frozen=True)
class GetMyDefaultAdministratorRights(Request):
    """\
    Represents GetMyDefaultAdministratorRights request object:
    https://core.telegram.org/bots/api#getmydefaultadministratorrights
    """

    for_channels: Optional[bool] = None

    def parse_result(self, data) -> ChatAdministratorRights:
        assert isinstance(data, dict), "Should be dict."

        return ChatAdministratorRights.parse(data)

    async def send(self) -> ChatAdministratorRights:
        res = await context.bot.send(self)

        return res.result
