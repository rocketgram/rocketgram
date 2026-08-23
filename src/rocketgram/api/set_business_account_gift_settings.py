# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass

from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class SetBusinessAccountGiftSettings(BoolResultMixin, Request):
    """\
    Represents SetBusinessAccountGiftSettings request object:
    https://core.telegram.org/bots/api#setbusinessaccountgiftsettings
    """

    business_connection_id: str
    show_gift_button: bool
    accepted_gift_types: dict
