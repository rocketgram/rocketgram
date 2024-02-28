# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional

from .forum_topic import ForumTopic
from .request import Request
from .. import context


@dataclass(frozen=True)
class CreateForumTopic(Request):
    """\
    Represents CreateForumTopic request object:
    https://core.telegram.org/bots/api#createforumtopic
    """

    chat_id: Union[int, str]
    name: str
    icon_color: Optional[int] = None
    icon_custom_emoji_id: Optional[str] = None

    def parse_result(self, data) -> ForumTopic:
        assert isinstance(data, dict), "Should be dict."
        return ForumTopic.parse(data)

    async def send(self) -> ForumTopic:
        res = await context.bot.send(self)
        return res.result
