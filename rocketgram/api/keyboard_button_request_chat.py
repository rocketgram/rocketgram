# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .chat_administrator_rights import ChatAdministratorRights


@dataclass(frozen=True)
class KeyboardButtonRequestChat:
    """\
    Represents KeyboardButtonRequestChat keyboard object:
    https://core.telegram.org/bots/api#keyboardbuttonrequestchat
    """

    request_id: int
    chat_is_channel: Optional[bool] = None
    chat_is_forum: Optional[bool] = None
    chat_has_username: Optional[bool] = None
    chat_is_created: Optional[bool] = None
    user_administrator_rights: Optional[ChatAdministratorRights] = None
    bot_administrator_rights: Optional[ChatAdministratorRights] = None
    bot_is_member: Optional[bool] = None
