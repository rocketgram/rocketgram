# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .user import User


@dataclass(frozen=True)
class ManagedBotCreated:
    """\
    Represents ManagedBotCreated object:
    https://core.telegram.org/bots/api#managedbotcreated
    """

    bot: User

    @classmethod
    def parse(cls, data: dict) -> Optional['ManagedBotCreated']:
        if data is None:
            return None
        return cls(User.parse(data['bot']))
