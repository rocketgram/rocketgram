# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, Dict


@dataclass(frozen=True)
class BotDescription:
    """\
    Represents BotDescription keyboard object:
    https://core.telegram.org/bots/api#botdescription
    """

    description: str

    @classmethod
    def parse(cls, data: Optional[Dict]) -> Optional['BotDescription']:
        if data is None:
            return None

        return cls(description=data['description'])
