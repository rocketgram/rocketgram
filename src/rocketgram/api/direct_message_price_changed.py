# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class DirectMessagePriceChanged:
    """\
    Represents DirectMessagePriceChanged object:
    https://core.telegram.org/bots/api#directmessagepricechanged
    """

    are_direct_messages_enabled: bool
    direct_message_star_count: Optional[int]

    @classmethod
    def parse(cls, data: dict) -> Optional['DirectMessagePriceChanged']:
        if data is None:
            return None

        return cls(
            data['are_direct_messages_enabled'],
            data.get('direct_message_star_count'),
        )
