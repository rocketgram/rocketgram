# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .background_type import BackgroundType


@dataclass(frozen=True)
class ChatBackground:
    """    Represents ChatBackground object:
    https://core.telegram.org/bots/api#chatbackground
    """

    type: BackgroundType

    @classmethod
    def parse(cls, data: dict) -> Optional['ChatBackground']:
        if data is None:
            return None

        return cls(BackgroundType.parse(data['type']))
