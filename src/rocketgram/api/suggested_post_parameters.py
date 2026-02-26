# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .suggested_post_price import SuggestedPostPrice


@dataclass(frozen=True)
class SuggestedPostParameters:
    """\
    Represents SuggestedPostParameters object:
    https://core.telegram.org/bots/api#suggestedpostparameters
    """

    price: Optional[SuggestedPostPrice] = None
    send_date: Optional[int] = None
