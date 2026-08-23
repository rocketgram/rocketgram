# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .user import User


@dataclass(frozen=True)
class BotSubscriptionUpdated:
    """\
    Represents BotSubscriptionUpdated object:
    https://core.telegram.org/bots/api#botsubscriptionupdated
    """

    user: User
    invoice_payload: str
    state: str

    @classmethod
    def parse(cls, data: dict) -> Optional['BotSubscriptionUpdated']:
        if data is None:
            return None

        return cls(User.parse(data['user']), data['invoice_payload'], data['state'])
