# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class ResponseParameters:
    """\
    Represents ResponseParameters object:
    https://core.telegram.org/bots/api#responseparameters
    """

    migrate_to_chat_id: int
    retry_after: int

    @classmethod
    def parse(cls, data: dict) -> Optional['ResponseParameters']:
        if data is None:
            return None

        return cls(data['migrate_to_chat_id'], data['retry_after'])
