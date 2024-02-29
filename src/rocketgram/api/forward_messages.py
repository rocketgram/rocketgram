# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional, List

from .message_id import MessageId
from .request import Request
from .utils import MessageResultMixin
from .. import context


@dataclass(frozen=True)
class ForwardMessages(MessageResultMixin, Request):
    """\
    Represents ForwardMessages request object:
    https://core.telegram.org/bots/api#forwardmessages
    """

    chat_id: Union[int, str]
    from_chat_id: Union[int, str]
    message_ids: List[int]
    message_thread_id: Optional[int] = None
    disable_notification: Optional[bool] = None
    protect_content: Optional[bool] = None

    def parse_result(self, data) -> List[MessageId]:
        assert isinstance(data, list), "Should be list."
        return [MessageId.parse(i) for i in data]

    async def send(self) -> List[MessageId]:
        res = await context.bot.send(self)
        return res.result
