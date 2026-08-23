# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import List, Optional

from .photo_size import PhotoSize


@dataclass(frozen=True)
class ChatShared:
    """\
    Represents ChatShared object:
    https://core.telegram.org/bots/api#chatshared
    """

    request_id: int
    chat_id: int
    title: Optional[str]
    username: Optional[str]
    photo: Optional[List[PhotoSize]]

    @classmethod
    def parse(cls, data: dict) -> Optional['ChatShared']:
        if data is None:
            return None

        return cls(
            data['request_id'],
            data['chat_id'],
            data.get('title'),
            data.get('username'),
            [PhotoSize.parse(d) for d in data['photo']] if 'photo' in data else None,
        )
