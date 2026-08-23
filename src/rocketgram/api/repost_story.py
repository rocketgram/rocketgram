# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .request import Request
from .utils import StoryResultMixin


@dataclass(frozen=True)
class RepostStory(StoryResultMixin, Request):
    """\
    Represents RepostStory request object:
    https://core.telegram.org/bots/api#repoststory
    """

    business_connection_id: str
    from_chat_id: int
    from_story_id: int
    active_period: int
    post_to_chat_page: Optional[bool] = None
    protect_content: Optional[bool] = None
