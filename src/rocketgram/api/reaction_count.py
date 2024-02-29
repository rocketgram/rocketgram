# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from . import reaction_type


@dataclass(frozen=True)
class ReactionCount:
    """\
    Represents ReactionCount object:
    https://core.telegram.org/bots/api#reactioncount
    """

    type: 'reaction_type.ReactionType'
    total_count: int

    @classmethod
    def parse(cls, data: dict) -> Optional['ReactionCount']:
        if data is None:
            return None

        return cls(
            reaction_type.ReactionType.parse(data['type']),
            data['total_count']
        )
