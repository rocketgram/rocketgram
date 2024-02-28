# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class ForumTopicCreated:
    """\
    Represents ForumTopicCreated object:
    https://core.telegram.org/bots/api#forumtopiccreated
    """

    name: str
    icon_color: int
    icon_custom_emoji_id: Optional[str]

    @classmethod
    def parse(cls, data: dict) -> Optional['ForumTopicCreated']:
        if data is None:
            return None

        return cls(data['name'], data['icon_color'], data.get('icon_custom_emoji_id'))
