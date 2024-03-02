# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Dict, Optional, List

from . import chat_boost


@dataclass(frozen=True)
class UserChatBoosts:
    """\
    Represents UserChatBoosts object:
    https://core.telegram.org/bots/api#userchatboosts
    """

    boosts: List['chat_boost.ChatBoost']

    @classmethod
    def parse(cls, data: Optional[Dict]) -> Optional['UserChatBoosts']:
        if data is None:
            return None

        boosts = [chat_boost.ChatBoost.parse(x) for x in data['boosts']]

        return cls(
            boosts
        )
