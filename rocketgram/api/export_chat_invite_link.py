# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union

from .request import Request
from .utils import StrResultMixin


@dataclass(frozen=True)
class ExportChatInviteLink(StrResultMixin, Request):
    """\
    Represents ExportChatInviteLink request object:
    https://core.telegram.org/bots/api#exportchatinvitelink
    """

    chat_id: Union[int, str]
