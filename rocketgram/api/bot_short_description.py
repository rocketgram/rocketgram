# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, Dict


@dataclass(frozen=True)
class BotShortDescription:
    """\
    Represents BotShortDescription keyboard object:
    https://core.telegram.org/bots/api#botshortdescription
    """

    short_description: str

    @classmethod
    def parse(cls, data: Optional[Dict]) -> Optional['BotShortDescription']:
        if data is None:
            return None

        return cls(short_description=data['short_description'])
