# Copyright (C) 2015-2021 by Vd.
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

    migrate_to_chat_id: Optional[int]
    retry_after: Optional[int]

    @classmethod
    def parse(cls, data: dict) -> Optional['ResponseParameters']:
        if data is None:
            return None

        return cls(data.get('migrate_to_chat_id'), data.get('retry_after'))
