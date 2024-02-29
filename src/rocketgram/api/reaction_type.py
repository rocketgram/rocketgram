# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .reaction_type_type import ReactionTypeType


@dataclass(frozen=True)
class ReactionType:
    """\
    Represents ReactionType object:
    https://core.telegram.org/bots/api#reactiontype
    """

    type: ReactionTypeType
    emoji: Optional[str] = None
    custom_emoji_id: Optional[str] = None

    @classmethod
    def parse(cls, data: dict) -> Optional['ReactionType']:
        if data is None:
            return None

        try:
            reaction_type_type = ReactionTypeType(data['type'])
        except ValueError:
            reaction_type_type = ReactionTypeType.unknown

        return cls(
            reaction_type_type,
            data.get("emoji"),
            data.get("custom_emoji_id"),
        )
