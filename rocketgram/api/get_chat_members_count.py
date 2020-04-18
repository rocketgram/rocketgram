# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union

from .request import Request
from .utils import IntResultMixin


@dataclass(frozen=True)
class GetChatMembersCount(IntResultMixin, Request):
    """\
    Represents GetChatMembersCount request object:
    https://core.telegram.org/bots/api#getchatmemberscount
    """

    chat_id: Union[int, str]
