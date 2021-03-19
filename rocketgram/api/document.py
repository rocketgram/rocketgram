# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .photo_size import PhotoSize


@dataclass(frozen=True)
class Document:
    """\
    Represents Document object:
    https://core.telegram.org/bots/api#document
    """

    file_id: str
    file_unique_id: str
    thumb: Optional[PhotoSize]
    file_name: Optional[str]
    mime_type: Optional[str]
    file_size: Optional[int]

    @classmethod
    def parse(cls, data: dict) -> Optional['Document']:
        if data is None:
            return None

        return cls(data['file_id'], data['file_unique_id'], PhotoSize.parse(data.get('thumb')), data.get('file_name'),
                   data.get('mime_type'), data.get('file_size'))
