# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .location_address import LocationAddress
from .reaction_type import ReactionType
from .story_area_type_type import StoryAreaTypeType


@dataclass(frozen=True)
class StoryAreaType:
    """\
    Represents StoryAreaType and its subtypes:
    https://core.telegram.org/bots/api#storyareatype
    """

    type: StoryAreaTypeType
    latitude: Optional[float]
    longitude: Optional[float]
    address: Optional[LocationAddress]
    reaction_type: Optional[ReactionType]
    is_dark: Optional[bool]
    is_flipped: Optional[bool]
    url: Optional[str]
    temperature: Optional[float]
    emoji: Optional[str]
    background_color: Optional[int]
    name: Optional[str]

    @classmethod
    def parse(cls, data: dict) -> Optional['StoryAreaType']:
        if data is None:
            return None

        try:
            type_ = StoryAreaTypeType(data['type'])
        except ValueError:
            type_ = StoryAreaTypeType.unknown

        return cls(
            type_,
            data.get('latitude'),
            data.get('longitude'),
            LocationAddress.parse(data.get('address')),
            ReactionType.parse(data.get('reaction_type')),
            data.get('is_dark'),
            data.get('is_flipped'),
            data.get('url'),
            data.get('temperature'),
            data.get('emoji'),
            data.get('background_color'),
            data.get('name'),
        )
