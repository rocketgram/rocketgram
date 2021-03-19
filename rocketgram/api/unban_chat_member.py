# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional

from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class UnbanChatMember(BoolResultMixin, Request):
    """\
    Represents UnbanChatMember request object:
    https://core.telegram.org/bots/api#unbanchatmember
    """

    chat_id: Union[int, str]
    user_id: int
    only_if_banned: Optional[bool]
