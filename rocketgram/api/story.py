# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from . import chat


@dataclass(frozen=True)
class Story:
    """\
    Represents Story object:
    https://core.telegram.org/bots/api#story
    """

    chat: 'chat.Chat'
    id: int

    @classmethod
    def parse(cls, data: dict) -> Optional['Story']:
        if data is None:
            return None

        return cls(
            chat.Chat.parse(data['chat']),
            data['id'],
        )
