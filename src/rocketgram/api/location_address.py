# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class LocationAddress:
    """    Represents LocationAddress object:
    https://core.telegram.org/bots/api#locationaddress
    """

    country_code: str
    state: Optional[str]
    city: Optional[str]
    street: Optional[str]

    @classmethod
    def parse(cls, data: dict) -> Optional['LocationAddress']:
        if data is None:
            return None

        return cls(data['country_code'], data.get('state'), data.get('city'), data.get('street'))
