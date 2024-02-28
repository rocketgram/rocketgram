# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from . import message


@dataclass(frozen=True)
class GiveawayCompleted:
    """\
    Represents GiveawayCompleted object:
    https://core.telegram.org/bots/api#giveawaycompleted
    """

    winner_count: int
    unclaimed_prize_count: Optional[int]
    giveaway_message: Optional['message.Message']

    @classmethod
    def parse(cls, data: dict) -> Optional['GiveawayCompleted']:
        if data is None:
            return None

        return cls(
            data['winner_count'],
            data['unclaimed_prize_count'],
            message.Message.parse(data.get('giveaway_message'))
        )
