# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass

from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class ConvertGiftToStars(BoolResultMixin, Request):
    """\
    Represents ConvertGiftToStars request object:
    https://core.telegram.org/bots/api#convertgifttostars
    """

    business_connection_id: str
    owned_gift_id: str
