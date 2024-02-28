# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional, List

from . import chat
from . import user


@dataclass(frozen=True)
class GiveawayWinners:
    """\
    Represents GiveawayWinners object:
    https://core.telegram.org/bots/api#giveawaywinners
    """

    chat: 'chat.Chat'
    giveaway_message_id: int
    winners_selection_date: datetime
    winner_count: int
    winners: List['user.User']
    additional_chat_count: Optional[int]
    premium_subscription_month_count: Optional[int]
    unclaimed_prize_count: Optional[int]
    only_new_members: Optional[bool]
    was_refunded: Optional[bool]
    prize_description: Optional[str]

    @classmethod
    def parse(cls, data: dict) -> Optional['GiveawayWinners']:
        if data is None:
            return None

        return cls(
            chat.Chat.parse(data['chat']),
            data['giveaway_message_id'],
            datetime.fromtimestamp(data['winners_selection_date'], tz=timezone.utc),
            data['winner_count'],
            [user.User.parse(u) for u in data['winners']],
            data.get('additional_chat_count'),
            data.get('premium_subscription_month_count'),
            data.get('unclaimed_prize_count'),
            data.get('only_new_members'),
            data.get('was_refunded'),
            data.get('prize_description')
        )
