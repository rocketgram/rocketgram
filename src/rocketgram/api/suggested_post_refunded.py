# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from . import message


@dataclass(frozen=True)
class SuggestedPostRefunded:
    """\
    Represents SuggestedPostRefunded object:
    https://core.telegram.org/bots/api#suggestedpostrefunded
    """

    suggested_post_message: Optional['message.Message']
    reason: str

    @classmethod
    def parse(cls, data: dict) -> Optional['SuggestedPostRefunded']:
        if data is None:
            return None

        return cls(
            message.Message.parse(data.get('suggested_post_message')),
            data['reason'],
        )
