# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class SentGuestMessage:
    """\
    Represents SentGuestMessage object:
    https://core.telegram.org/bots/api#sentguestmessage
    """

    inline_message_id: str

    @classmethod
    def parse(cls, data: dict) -> Optional['SentGuestMessage']:
        if data is None:
            return None

        return cls(data['inline_message_id'])
