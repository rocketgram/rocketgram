# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


import warnings
from dataclasses import dataclass
from typing import Optional

from .shipping_address import ShippingAddress
from .user import User


@dataclass(frozen=True)
class ShippingQuery:
    """\
    Represents ShippingQuery object:
    https://core.telegram.org/bots/api#successfulpayment

    Differences in field names:
    from -> user
    """

    id: str
    user: User
    invoice_payload: str
    shipping_address: ShippingAddress

    @classmethod
    def parse(cls, data: dict) -> Optional['ShippingQuery']:
        if data is None:
            return None

        return cls(data['id'], User.parse(data['from']), data['invoice_payload'],
                   ShippingAddress.parse(data['shipping_address']))

    @property
    def query_id(self) -> str:
        warnings.warn("This field is deprecated. Use `id` instead.", DeprecationWarning)

        return self.id
