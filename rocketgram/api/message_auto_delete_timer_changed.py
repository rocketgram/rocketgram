# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Dict, Optional


@dataclass(frozen=True)
class MessageAutoDeleteTimerChanged:
    """\
    Represents MessageAutoDeleteTimerChanged object:
    https://core.telegram.org/bots/api#messageautodeletetimerchanged
    """

    message_auto_delete_time: int

    @classmethod
    def parse(cls, data: Optional[Dict]) -> Optional['MessageAutoDeleteTimerChanged']:
        if data is None:
            return None

        return cls(data['message_auto_delete_time'])
