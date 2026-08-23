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

    unlimited_gifts: bool
    limited_gifts: bool
    unique_gifts: bool
    premium_subscription: bool
    gifts_from_channels: bool

    @classmethod
    def parse(cls, data: dict) -> Optional['AcceptedGiftTypes']:
        if data is None:
            return None

        return cls(
            data['unlimited_gifts'],
            data['limited_gifts'],
            data['unique_gifts'],
            data['premium_subscription'],
            data['gifts_from_channels'],
        )
