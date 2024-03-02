# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Dict, Optional


@dataclass(frozen=True)
class VideoChatEnded:
    """\
    Represents VideoChatEnded object:
    https://core.telegram.org/bots/api#videochatended
    """

    duration: int

    @classmethod
    def parse(cls, data: Optional[Dict]) -> Optional['VideoChatEnded']:
        if data is None:
            return None

        return cls(data['duration'])
