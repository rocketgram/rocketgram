# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class StoryAreaPosition:
    """\
    Represents StoryAreaPosition object:
    https://core.telegram.org/bots/api#storyareaposition
    """

    x_percentage: float
    y_percentage: float
    width_percentage: float
    height_percentage: float
    rotation_angle: float
    corner_radius_percentage: float

    @classmethod
    def parse(cls, data: dict) -> Optional['StoryAreaPosition']:
        if data is None:
            return None

        return cls(
            data['x_percentage'],
            data['y_percentage'],
            data['width_percentage'],
            data['height_percentage'],
            data['rotation_angle'],
            data['corner_radius_percentage'],
        )
