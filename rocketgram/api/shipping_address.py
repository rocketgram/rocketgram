# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class ShippingAddress:
    """\
    Represents ShippingAddress object:
    https://core.telegram.org/bots/api#shippingaddress
    """

    country_code: str
    state: str
    city: str
    street_line1: str
    street_line2: str
    post_code: str

    @classmethod
    def parse(cls, data: dict) -> Optional['ShippingAddress']:
        if data is None:
            return None

        return cls(data['country_code'], data['state'], data['city'], data['street_line1'],
                   data['street_line2'], data['post_code'])
