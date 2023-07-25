# Copyright (C) 2015-2023 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union

from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class ReopenGeneralForumTopic(BoolResultMixin, Request):
    """\
    Represents ReopenGeneralForumTopic request object:
    https://core.telegram.org/bots/api#reopengeneralforumtopic
    """

    chat_id: Union[int, str]
