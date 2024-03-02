# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from . import chat_boost_source_type
from . import user


@dataclass(frozen=True)
class ChatBoostSource:
    """\
    Represents ChatBoostSource, ChatBoostSourcePremium,
    ChatBoostSourceGiftCode, ChatBoostSourceGiveaway objects:
    https://core.telegram.org/bots/api#chatboostsource
    """

    source: 'chat_boost_source_type.ChatBoostSourceType'
    giveaway_message_id: Optional[int]
    user: Optional['user.User']
    is_unclaimed: Optional[bool]

    @classmethod
    def parse(cls, data: dict) -> Optional['ChatBoostSource']:
        if data is None:
            return None

        try:
            source_ = chat_boost_source_type.ChatBoostSourceType(data['source'])
        except ValueError:
            source_ = chat_boost_source_type.ChatBoostSourceType.unknown

        return cls(
            source_,
            data.get('giveaway_message_id'),
            user.User.parse(data.get('user')),
            data.get('is_unclaimed')
        )
