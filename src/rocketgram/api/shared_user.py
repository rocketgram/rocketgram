# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List

from .photo_size import PhotoSize


@dataclass(frozen=True)
class SharedUser:
    """\
    Represents SharedUser object:
    https://core.telegram.org/bots/api#shareduser
    """

    user_id: int
    first_name: Optional[str]
    last_name: Optional[str]
    username: Optional[str]
    photo: Optional[List[PhotoSize]]

    @classmethod
    def parse(cls, data: dict) -> Optional['SharedUser']:
        if data is None:
            return None

        return cls(
            data['user_id'],
            data.get('first_name'),
            data.get('last_name'),
            data.get('username'),
            [PhotoSize.parse(p) for p in data['photo']] if 'photo' in data else None,
        )
