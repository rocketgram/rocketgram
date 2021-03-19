# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, Dict


@dataclass(frozen=True)
class LoginUrl:
    """\
    Represents LoginUrl keyboard object:
    https://core.telegram.org/bots/api#loginurl
    """

    url: str
    forward_text: Optional[str] = None
    bot_username: Optional[str] = None
    request_write_access: Optional[bool] = None

    @classmethod
    def parse(cls, data: Optional[Dict]) -> Optional['LoginUrl']:
        if data is None:
            return None

        return cls(url=data['url'], forward_text=data.get('forward_text'), bot_username=data.get('bot_username'),
                   request_write_access=data.get('request_write_access'))
