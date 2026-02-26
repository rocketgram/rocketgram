# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class BusinessOpeningHoursInterval:
    """\
    Represents BusinessOpeningHoursInterval object:
    https://core.telegram.org/bots/api#businessopeninghoursinterval
    """

    opening_minute: int
    closing_minute: int

    @classmethod
    def parse(cls, data: dict) -> Optional['BusinessOpeningHoursInterval']:
        if data is None:
            return None

        return cls(
            data['opening_minute'],
            data['closing_minute'],
        )
