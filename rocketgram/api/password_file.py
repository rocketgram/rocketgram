# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(frozen=True)
class PassportFile:
    """\
    Represents PassportFile object:
    https://core.telegram.org/bots/api#passportfile
    """

    file_id: str
    file_unique_id: str
    file_size: int
    file_date: datetime

    @classmethod
    def parse(cls, data: dict) -> Optional['PassportFile']:
        if data is None:
            return None

        return cls(data['file_id'], data['file_unique_id'], data['file_size'],
                   datetime.utcfromtimestamp(data['file_date']))
