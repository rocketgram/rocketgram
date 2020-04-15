# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union
from .request import Request
from .chat_permissions import ChatPermissions


@dataclass(frozen=True)
class SetChatPermissions(Request):
    """\
    Represents SetChatPermissions request object:
    https://core.telegram.org/bots/api#setchatpermissions
    """

    method = "setChatPermissions"

    user_id: Union[int, str]
    permissions: ChatPermissions
