# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class RefundStarPayment(BoolResultMixin, Request):
    """    Represents RefundStarPayment request object:
    https://core.telegram.org/bots/api#refundstarpayment
    """

    user_id: int
    telegram_payment_charge_id: str
