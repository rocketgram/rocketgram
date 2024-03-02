# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List

from . import chat


@dataclass(frozen=True)
class Giveaway:
    """\
    Represents Giveaway object:
    https://core.telegram.org/bots/api#giveaway
    """

    chats: List['chat.Chat']
    winners_selection_date: int
    winner_count: int
    only_new_members: Optional[bool]
    has_public_winners: Optional[bool]
    prize_description: Optional[str]
    country_codes: Optional[List[str]]
    premium_subscription_month_count: Optional[int]

    @classmethod
    def parse(cls, data: dict) -> Optional['Giveaway']:
        if data is None:
            return None

        return cls(
            [chat.Chat.parse(c) for c in data['chats']],
            data['winners_selection_date'],
            data['winner_count'],
            data.get('only_new_members'),
            data.get('has_public_winners'),
            data.get('prize_description'),
            data.get('country_codes'),
            data.get('premium_subscription_month_count')
        )
