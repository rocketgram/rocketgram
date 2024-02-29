# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class ChatBoostAdded:
    """\
    Represents ChatBoostAdded object:
    https://core.telegram.org/bots/api#chatboostadded
    """

    boost_count: int

    @classmethod
    def parse(cls, data: dict) -> Optional['ChatBoostAdded']:
        if data is None:
            return None

        return cls(
            data['boost_count'],
        )
