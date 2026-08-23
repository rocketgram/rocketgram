# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class RefundedPayment:
    """    Represents RefundedPayment object:
    https://core.telegram.org/bots/api#refundedpayment
    """

    currency: str
    total_amount: int
    invoice_payload: str
    telegram_payment_charge_id: str
    provider_payment_charge_id: Optional[str]

    @classmethod
    def parse(cls, data: dict) -> Optional['RefundedPayment']:
        if data is None:
            return None

        return cls(
            data['currency'],
            data['total_amount'],
            data['invoice_payload'],
            data['telegram_payment_charge_id'],
            data.get('provider_payment_charge_id')
        )
