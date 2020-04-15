# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional

from .request import Request


@dataclass(frozen=True)
class SetChatDescription(Request):
    """\
    Represents SetChatDescription request object:
    https://core.telegram.org/bots/api#setchatdescription
    """

    method = "setChatDescription"

    chat_id: Union[int, str]
    description: Optional[str]
