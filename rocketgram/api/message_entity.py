# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


import warnings
from dataclasses import dataclass
from typing import Optional

from .entity_type import EntityType
from .user import User


@dataclass(frozen=True)
class MessageEntity:
    """\
    Represents MessageEntity object:
    https://core.telegram.org/bots/api#messageentity
    """

    type: EntityType
    offset: int
    length: int
    url: Optional[str]
    user: Optional[User]
    language: Optional[str]

    @classmethod
    def parse(cls, data: dict) -> Optional['MessageEntity']:
        if data is None:
            return None

        try:
            entity_type = EntityType(data['type'])
        except ValueError:
            entity_type = EntityType.unknown

        return cls(entity_type, data['offset'], data['length'], data.get('url'),
                   User.parse(data.get('user')), data.get('language'))

    @property
    def entity_type(self) -> EntityType:
        warnings.warn("This field is deprecated. Use `type` instead.", DeprecationWarning)

        return self.type
