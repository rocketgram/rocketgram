# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .story_area_position import StoryAreaPosition
from .story_area_type import StoryAreaType


@dataclass(frozen=True)
class StoryArea:
    """\
    Represents StoryArea object:
    https://core.telegram.org/bots/api#storyarea
    """

    position: StoryAreaPosition
    type: StoryAreaType

    @classmethod
    def parse(cls, data: dict) -> Optional['StoryArea']:
        if data is None:
            return None

        return cls(
            StoryAreaPosition.parse(data['position']),
            StoryAreaType.parse(data['type']),
        )
