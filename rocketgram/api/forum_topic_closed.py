# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class ForumTopicClosed:
    """\
    Represents ForumTopicClosed object:
    https://core.telegram.org/bots/api#forumtopicclosed
    """

    @classmethod
    def parse(cls, data: dict) -> Optional['ForumTopicClosed']:
        return cls() if data else None
