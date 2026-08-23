# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .community import Community


@dataclass(frozen=True)
class CommunityChatAdded:
    """\
    Represents CommunityChatAdded object:
    https://core.telegram.org/bots/api#communitychatadded
    """

    community: Community

    @classmethod
    def parse(cls, data: dict) -> Optional['CommunityChatAdded']:
        if data is None:
            return None

        return cls(Community.parse(data['community']))
