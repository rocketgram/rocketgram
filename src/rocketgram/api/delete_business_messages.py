# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class DeleteBusinessMessages(BoolResultMixin, Request):
    """    Represents DeleteBusinessMessages request object:
    https://core.telegram.org/bots/api#deletebusinessmessages
    """

    business_connection_id: str
    message_ids: list
