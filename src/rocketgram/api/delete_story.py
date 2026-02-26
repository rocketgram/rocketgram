# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass

from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class DeleteStory(BoolResultMixin, Request):
    """    Represents DeleteStory request object:
    https://core.telegram.org/bots/api#deletestory
    """

    business_connection_id: str
    story_id: int
