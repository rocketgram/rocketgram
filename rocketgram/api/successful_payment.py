# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .order_info import OrderInfo


@dataclass(frozen=True)
class SuccessfulPayment:
    """\
    Represents SuccessfulPayment object:
    https://core.telegram.org/bots/api#successfulpayment
    """

    currency: str
    total_amount: int
    invoice_payload: str
    shipping_option_id: Optional[str]
    order_info: Optional[OrderInfo]
    telegram_payment_charge_id: str
    provider_payment_charge_id: str

    @classmethod
    def parse(cls, data: dict) -> Optional['SuccessfulPayment']:
        if data is None:
            return None

        return cls(data['currency'], data['total_amount'], data['invoice_payload'], data.get('shipping_option_id'),
                   OrderInfo.parse(data.get('order_info')), data['telegram_payment_charge_id'],
                   data['provider_payment_charge_id'])
