# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List

from .audio import Audio


@dataclass(frozen=True)
class UserProfileAudios:
    """    Represents UserProfileAudios object:
    https://core.telegram.org/bots/api#userprofileaudios
    """

    total_count: int
    audios: List[Audio]

    @classmethod
    def parse(cls, data: dict) -> Optional['UserProfileAudios']:
        if data is None:
            return None

        return cls(
            data['total_count'],
            [Audio.parse(a) for a in data['audios']],
        )
