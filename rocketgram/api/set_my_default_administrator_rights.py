# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .chat_administrator_rights import ChatAdministratorRights
from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class SetMyDefaultAdministratorRights(BoolResultMixin, Request):
    """\
    Represents SetMyDefaultAdministratorRights request object:
    https://core.telegram.org/bots/api#setmydefaultadministratorrights
    """

    rights: Optional[ChatAdministratorRights] = None
    for_channels: Optional[bool] = None
