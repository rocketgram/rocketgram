# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List

from .business_opening_hours_interval import BusinessOpeningHoursInterval


@dataclass(frozen=True)
class BusinessOpeningHours:
    """\
    Represents BusinessOpeningHours object:
    https://core.telegram.org/bots/api#businessopeninghours
    """

    time_zone_name: str
    opening_hours: List[BusinessOpeningHoursInterval]

    @classmethod
    def parse(cls, data: dict) -> Optional['BusinessOpeningHours']:
        if data is None:
            return None

        return cls(
            data['time_zone_name'],
            [BusinessOpeningHoursInterval.parse(i) for i in data['opening_hours']],
        )
