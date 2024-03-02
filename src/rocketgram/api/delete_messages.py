# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, List

from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class DeleteMessages(BoolResultMixin, Request):
    """\
    Represents DeleteMessages request object:
    https://core.telegram.org/bots/api#deletemessages
    """

    chat_id: Union[int, str] = None
    message_ids: List[int] = None
