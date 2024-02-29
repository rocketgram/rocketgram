# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional, List

from . import reply_parameters
from .message_entity import MessageEntity
from .message_id import MessageId
from .parse_mode_type import ParseModeType
from .request import Request
from .utils import AnyKeyboard
from ..context import context


@dataclass(frozen=True)
class CopyMessage(Request):
    """\
    Represents CopyMessage request object:
    https://core.telegram.org/bots/api#copymessage
    """

    chat_id: Union[int, str]
    from_chat_id: Union[int, str]
    message_id: int
    message_thread_id: Optional[int] = None
    caption: Optional[str] = None
    parse_mode: Optional[ParseModeType] = None
    caption_entities: Optional[List[MessageEntity]] = None
    disable_notification: Optional[bool] = None
    protect_content: Optional[bool] = None
    reply_parameters: Optional['reply_parameters.ReplyParameters'] = None
    reply_markup: Optional[AnyKeyboard] = None

    def parse_result(self, data) -> MessageId:
        assert isinstance(data, dict), "Should be dict."
        return MessageId.parse(data)

    async def send(self) -> MessageId:
        res = await context.bot.send(self)
        return res.result
