# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Voice:
    """\
    Represents Voice object:
    https://core.telegram.org/bots/api#voice
    """

    file_id: str
    file_unique_id: str
    duration: int
    mime_type: Optional[str]
    file_size: Optional[int]

    @classmethod
    def parse(cls, data: dict) -> Optional['Voice']:
        if data is None:
            return None

        return cls(data['file_id'], data['file_unique_id'], data['duration'], data.get('mime_type'),
                   data.get('file_size'))
