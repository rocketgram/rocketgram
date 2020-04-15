# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union

from .request import Request


@dataclass(frozen=True)
class DeleteMessage(Request):
    """\
    Represents DeleteMessage request object:
    https://core.telegram.org/bots/api#deletemessage
    """

    method = "deleteMessage"

    chat_id: Union[int, str] = None
    message_id: int = None
