# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List

from . import chat
from . import user
from .affiliate_info import AffiliateInfo
from .gift import Gift
from .paid_media import PaidMedia
from .revenue_withdrawal_state import RevenueWithdrawalState
from .transaction_partner_type import TransactionPartnerType


@dataclass(frozen=True)
class TransactionPartner:
    """\
    Represents TransactionPartner and its subtypes:
    https://core.telegram.org/bots/api#transactionpartner
    """

    type: TransactionPartnerType
    user: Optional['user.User']
    chat: Optional['chat.Chat']
    affiliate: Optional[AffiliateInfo]
    invoice_payload: Optional[str]
    paid_media: Optional[List[PaidMedia]]
    paid_media_payload: Optional[str]
    subscription_period: Optional[int]
    gift: Optional[Gift]
    withdrawal_state: Optional[RevenueWithdrawalState]
    commission_per_mille: Optional[int]
    request_count: Optional[int]
    sponsor_user: Optional['user.User']

    @classmethod
    def parse(cls, data: dict) -> Optional['TransactionPartner']:
        if data is None:
            return None

        try:
            partner_type = TransactionPartnerType(data['type'])
        except ValueError:
            partner_type = TransactionPartnerType.unknown

        return cls(
            partner_type,
            user.User.parse(data.get('user')),
            chat.Chat.parse(data.get('chat')),
            AffiliateInfo.parse(data.get('affiliate')),
            data.get('invoice_payload'),
            [PaidMedia.parse(p) for p in data['paid_media']] if 'paid_media' in data else None,
            data.get('paid_media_payload'),
            data.get('subscription_period'),
            Gift.parse(data.get('gift')),
            RevenueWithdrawalState.parse(data.get('withdrawal_state')),
            data.get('commission_per_mille'),
            data.get('request_count'),
            user.User.parse(data.get('sponsor_user')),
        )
