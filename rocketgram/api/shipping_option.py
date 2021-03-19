# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import List

from .labeled_price import LabeledPrice


@dataclass(frozen=True)
class ShippingOption:
    """\
    Represents ShippingOption object:
    https://core.telegram.org/bots/api#shippingoption
    """

    id: str
    title: str
    prices: List[LabeledPrice]
