# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass

from .request import Request
from .. import api


@dataclass(frozen=True)
class GetWebhookInfo(Request):
    """\
    Represents GetWebhookInfo request object:
    https://core.telegram.org/bots/api#getwebhookinfo
    """

    def parse_result(self, data) -> 'api.WebhookInfo':
        assert isinstance(data, dict), "Should be dict."
        return api.WebhookInfo.parse(data)

    async def send2(self) -> 'api.WebhookInfo':
        res = await self._send()
        return res.result
