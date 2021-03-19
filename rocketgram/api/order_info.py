# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .shipping_address import ShippingAddress


@dataclass(frozen=True)
class OrderInfo:
    """\
    Represents OrderInfo object:
    https://core.telegram.org/bots/api#orderinfo
    """

    name: Optional[str]
    phone_number: Optional[str]
    email: Optional[str]
    shipping_address: Optional[ShippingAddress]

    @classmethod
    def parse(cls, data: dict) -> Optional['OrderInfo']:
        if data is None:
            return None

        return cls(data.get('name'), data.get('phone_number'), data.get('email'),
                   ShippingAddress.parse(data.get('shipping_address')))
