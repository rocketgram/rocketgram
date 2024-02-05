# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class ForumTopicEdited:
    """\
    Represents ForumTopicEdited object:
    https://core.telegram.org/bots/api#forumtopicedited
    """

    name: Optional[str]
    icon_custom_emoji_id: Optional[str]

    @classmethod
    def parse(cls, data: dict) -> Optional['ForumTopicEdited']:
        if data is None:
            return None

        return cls(
            data.get('name'),
            data.get('icon_custom_emoji_id')
        )
