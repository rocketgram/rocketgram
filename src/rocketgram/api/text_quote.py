# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List

from . import message_entity


@dataclass(frozen=True)
class TextQuote:
    """\
    Represents TextQuote object:
    https://core.telegram.org/bots/api#textquote
    """

    text: str
    entities: Optional[List['message_entity.MessageEntity']]
    position: int
    is_manual: Optional[bool]

    @classmethod
    def parse(cls, data: dict) -> Optional['TextQuote']:
        if data is None:
            return None

        return cls(
            data['text'],
            [message_entity.MessageEntity.parse(e) for e in data['entities']] if 'entities' in data else None,
            data['position'],
            data.get('is_manual')
        )
