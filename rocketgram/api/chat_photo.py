# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Dict, Optional


@dataclass(frozen=True)
class ChatPhoto:
    """\
    Represents ChatPhoto object:
    https://core.telegram.org/bots/api#chatphoto
    """

    small_file_id: str
    small_file_unique_id: str
    big_file_id: str
    big_file_unique_id: str

    @classmethod
    def parse(cls, data: Optional[Dict]) -> Optional['ChatPhoto']:
        if data is None:
            return None

        return cls(data['small_file_id'], data['small_file_unique_id'], data['big_file_id'], data['big_file_unique_id'])
