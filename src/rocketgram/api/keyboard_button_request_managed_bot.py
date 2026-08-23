# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class KeyboardButtonRequestManagedBot:
    """\
    Represents KeyboardButtonRequestManagedBot object:
    https://core.telegram.org/bots/api#keyboardbuttonrequestmanagedbot
    """

    request_id: int
    suggested_name: Optional[str] = None
    suggested_username: Optional[str] = None
