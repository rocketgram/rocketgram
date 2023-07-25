# Copyright (C) 2015-2023 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class WriteAccessAllowed:
    """\
    Represents WriteAccessAllowed object:
    https://core.telegram.org/bots/api#writeaccessallowed
    """

    @classmethod
    def parse(cls, data: dict) -> Optional['WriteAccessAllowed']:
        if data is None:
            return None

        return cls()
