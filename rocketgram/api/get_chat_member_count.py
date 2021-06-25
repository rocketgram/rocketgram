# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union

from .request import Request
from .utils import IntResultMixin


@dataclass(frozen=True)
class GetChatMemberCount(IntResultMixin, Request):
    """\
    Represents GetChatMemberCount request object:
    https://core.telegram.org/bots/api#getchatmemberscount
    """

    chat_id: Union[int, str]


GetChatMembersCount = GetChatMemberCount  # Deprecated! Will be removed in version 4.
