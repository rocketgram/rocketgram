# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class ForumTopicReopened:
    """\
    Represents ForumTopicReopened object:
    https://core.telegram.org/bots/api#forumtopicreopened
    """

    @classmethod
    def parse(cls, data: dict) -> Optional['ForumTopicReopened']:
        return cls() if data else None
