# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from . import chat
from . import user


@dataclass(frozen=True)
class AffiliateInfo:
    """\
    Represents AffiliateInfo object:
    https://core.telegram.org/bots/api#affiliateinfo
    """

    affiliate_user: Optional[user.User]
    affiliate_chat: Optional[chat.Chat]
    commission_per_mille: int
    amount: int
    nanostar_amount: Optional[int]

    @classmethod
    def parse(cls, data: dict) -> Optional['AffiliateInfo']:
        if data is None:
            return None

        return cls(
            user.User.parse(data.get('affiliate_user')),
            chat.Chat.parse(data.get('affiliate_chat')),
            data['commission_per_mille'],
            data['amount'],
            data.get('nanostar_amount'),
        )
