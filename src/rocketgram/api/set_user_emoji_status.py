# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class SetUserEmojiStatus(BoolResultMixin, Request):
    """\
    Represents SetUserEmojiStatus request object:
    https://core.telegram.org/bots/api#setuseremojistatus
    """

    user_id: int
    emoji_status_custom_emoji_id: Optional[str] = None
    emoji_status_expiration_date: Optional[int] = None
