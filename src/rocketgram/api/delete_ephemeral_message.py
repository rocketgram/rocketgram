# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union

from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class DeleteEphemeralMessage(BoolResultMixin, Request):
    """\
    Represents DeleteEphemeralMessage request object:
    https://core.telegram.org/bots/api#deleteephemeralmessage
    """

    chat_id: Union[int, str]
    receiver_user_id: int
    ephemeral_message_id: int
