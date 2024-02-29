# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, List, Optional

from . import reaction_type
from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class SetMessageReaction(BoolResultMixin, Request):
    """\
    Represents SetMessageReaction request object:
    https://core.telegram.org/bots/api#setmessagereaction
    """

    chat_id: Union[int, str]
    message_id: int
    reaction: Optional[List['reaction_type.ReactionType']] = None
    is_big: Optional[bool] = None
