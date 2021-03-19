# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union

from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class DeleteMessage(BoolResultMixin, Request):
    """\
    Represents DeleteMessage request object:
    https://core.telegram.org/bots/api#deletemessage
    """

    chat_id: Union[int, str] = None
    message_id: int = None
