# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class PollOption:
    """\
    Represents PollOption object:
    https://core.telegram.org/bots/api#polloption
    """

    text: str
    voter_count: int

    @classmethod
    def parse(cls, data: dict) -> Optional['PollOption']:
        if data is None:
            return None

        return cls(data['text'], data['voter_count'])
