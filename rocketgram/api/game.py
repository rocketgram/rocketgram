# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import List, Optional

from .animation import Animation
from .message_entity import MessageEntity
from .photo_size import PhotoSize


@dataclass(frozen=True)
class Game:
    """\
    Represents Game object:
    https://core.telegram.org/bots/api#game
    """

    title: str
    description: str
    photo: List[PhotoSize]
    text: Optional[str]
    text_entities: Optional[List[MessageEntity]]
    animation: Optional[Animation]

    @classmethod
    def parse(cls, data: dict) -> Optional['Game']:
        if data is None:
            return None

        photo = [PhotoSize.parse(s) for s in data['photo']]
        text_entities = [MessageEntity.parse(s) for s in data['text_entities']] if 'text_entities' in data else None

        return cls(data['title'], data['description'], photo, data.get('text'),
                   text_entities, Animation.parse(data.get('animation')))
