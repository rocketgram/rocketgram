# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional

from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class VerifyChat(BoolResultMixin, Request):
    """\
    Represents VerifyChat request object:
    https://core.telegram.org/bots/api#verifychat
    """

    chat_id: Union[int, str]
    custom_description: Optional[str] = None
