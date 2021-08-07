# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


import warnings
from dataclasses import dataclass
from typing import Optional

from .order_info import OrderInfo
from .user import User


@dataclass(frozen=True)
class PreCheckoutQuery:
    """\
    Represents PreCheckoutQuery object:
    https://core.telegram.org/bots/api#precheckoutquery

    Differences in field names:
    from -> user
    """

    id: str
    user: User
    currency: str
    total_amount: int
    invoice_payload: str
    shipping_option_id: Optional[str]
    order_info: Optional[OrderInfo]

    @classmethod
    def parse(cls, data: dict) -> Optional['PreCheckoutQuery']:
        if data is None:
            return None

        return cls(data['id'], User.parse(data['from']), data['currency'], data['total_amount'],
                   data['invoice_payload'], data.get('shipping_option_id'),
                   OrderInfo.parse(data.get('order_info')))

    @property
    def query_id(self) -> str:
        warnings.warn("This field is deprecated. Use `id` instead.", DeprecationWarning)

        return self.id
