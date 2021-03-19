# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Contact:
    """\
    Represents Contact object:
    https://core.telegram.org/bots/api#contact
    """

    phone_number: str
    first_name: str
    last_name: Optional[str]
    user_id: Optional[int]
    vcard: Optional[str]

    @classmethod
    def parse(cls, data: dict) -> Optional['Contact']:
        if data is None:
            return None

        return cls(data['phone_number'], data['first_name'], data.get('last_name'),
                   data.get('user_id'), data.get('vcard'))
