# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class ChatShared:
    """\
    Represents ChatShared object:
    https://core.telegram.org/bots/api#chatshared
    """

    request_id: int
    chat_id: int

    @classmethod
    def parse(cls, data: dict) -> Optional['ChatShared']:
        if data is None:
            return None

        return cls(data['request_id'], data['chat_id'])
