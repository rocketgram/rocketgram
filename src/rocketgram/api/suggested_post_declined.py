# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from . import message


@dataclass(frozen=True)
class SuggestedPostDeclined:
    """\
    Represents SuggestedPostDeclined object:
    https://core.telegram.org/bots/api#suggestedpostdeclined
    """

    suggested_post_message: Optional['message.Message']
    comment: Optional[str]

    @classmethod
    def parse(cls, data: dict) -> Optional['SuggestedPostDeclined']:
        if data is None:
            return None

        return cls(
            message.Message.parse(data.get('suggested_post_message')),
            data.get('comment'),
        )
