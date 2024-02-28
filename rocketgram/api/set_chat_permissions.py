# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional

from .chat_permissions import ChatPermissions
from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class SetChatPermissions(BoolResultMixin, Request):
    """\
    Represents SetChatPermissions request object:
    https://core.telegram.org/bots/api#setchatpermissions
    """

    user_id: Union[int, str]
    permissions: ChatPermissions
    use_independent_chat_permissions: Optional[bool] = None
