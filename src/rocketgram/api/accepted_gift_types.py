# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class AcceptedGiftTypes:
    """\
    Represents AcceptedGiftTypes object:
    https://core.telegram.org/bots/api#acceptedgifttypes
    """

    unlimited_gifts: Optional[bool]
    limited_gifts: Optional[bool]
    unique_gifts: Optional[bool]
    premium_subscription: Optional[bool]
    gifts_from_channels: Optional[bool]

    @classmethod
    def parse(cls, data: dict) -> Optional['AcceptedGiftTypes']:
        if data is None:
            return None

        return cls(
            data.get('unlimited_gifts'),
            data.get('limited_gifts'),
            data.get('unique_gifts'),
            data.get('premium_subscription'),
            data.get('gifts_from_channels'),
        )
