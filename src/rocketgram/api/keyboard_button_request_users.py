# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class KeyboardButtonRequestUsers:
    """\
    Represents KeyboardButtonRequestUser keyboard object:
    https://core.telegram.org/bots/api#keyboardbuttonrequestuser
    """

    request_id: int
    user_is_bot: Optional[bool] = None
    user_is_premium: Optional[bool] = None
    max_quantity: Optional[int] = None
