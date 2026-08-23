# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List

from .message_entity import MessageEntity
from .parse_mode_type import ParseModeType
from .request import Request
from .story_area import StoryArea
from .utils import BoolResultMixin


@dataclass(frozen=True)
class EditStory(BoolResultMixin, Request):
    """    Represents EditStory request object:
    https://core.telegram.org/bots/api#editstory
    """

    business_connection_id: str
    story_id: int
    content: dict  # InputStoryContent
    caption: Optional[str] = None
    parse_mode: Optional[ParseModeType] = None
    caption_entities: Optional[List[MessageEntity]] = None
    areas: Optional[List[StoryArea]] = None
