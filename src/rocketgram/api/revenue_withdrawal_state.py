# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .revenue_withdrawal_state_type import RevenueWithdrawalStateType


@dataclass(frozen=True)
class RevenueWithdrawalState:
    """\
    Represents RevenueWithdrawalState, RevenueWithdrawalStatePending,
    RevenueWithdrawalStateSucceeded, RevenueWithdrawalStateFailed objects:
    https://core.telegram.org/bots/api#revenuewithdrawalstate
    """

    type: RevenueWithdrawalStateType
    date: Optional[int]
    url: Optional[str]

    @classmethod
    def parse(cls, data: dict) -> Optional['RevenueWithdrawalState']:
        if data is None:
            return None

        try:
            state_type = RevenueWithdrawalStateType(data['type'])
        except ValueError:
            state_type = RevenueWithdrawalStateType.unknown

        return cls(
            state_type,
            data.get('date'),
            data.get('url'),
        )
