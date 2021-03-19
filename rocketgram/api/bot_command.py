# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class BotCommand:
    """\
    Represents BotCommand object:
    https://core.telegram.org/bots/api#botcommand
    """

    command: str
    description: str

    @classmethod
    def parse(cls, data: dict) -> Optional['BotCommand']:
        if data is None:
            return None

        return cls(data['command'], data['description'])
