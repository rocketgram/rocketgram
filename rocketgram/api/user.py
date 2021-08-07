# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


import warnings
from dataclasses import dataclass
from typing import Dict, Optional


@dataclass(frozen=True)
class User:
    """\
    Represents User object:
    https://core.telegram.org/bots/api#user
    """

    id: int
    is_bot: bool
    first_name: str
    last_name: Optional[str]
    username: Optional[str]
    language_code: Optional[str]
    can_join_groups: Optional[bool]
    can_read_all_group_messages: Optional[bool]
    supports_inline_queries: Optional[bool]

    @classmethod
    def parse(cls, data: Optional[Dict]) -> Optional['User']:
        if data is None:
            return None

        return cls(data['id'], data['is_bot'], data['first_name'], data.get('last_name'), data.get('username'),
                   data.get('language_code'), data.get('can_join_groups'), data.get('can_read_all_group_messages'),
                   data.get('supports_inline_queries'))

    @property
    def user_id(self) -> int:
        warnings.warn("This field is deprecated. Use `id` instead.", DeprecationWarning)

        return self.id
