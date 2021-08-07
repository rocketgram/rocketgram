# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional, List

from .message_entity import MessageEntity
from .message_id import MessageId
from .parse_mode_type import ParseModeType
from .request import Request
from .utils import ALL_KEYBOARDS
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
    caption: Optional[str] = None
    parse_mode: Optional[ParseModeType] = None
    caption_entities: Optional[List[MessageEntity]] = None
    disable_notification: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    allow_sending_without_reply: Optional[bool] = None
    reply_markup: Optional[ALL_KEYBOARDS] = None

    def parse_result(self, data) -> MessageId:
        assert isinstance(data, dict), "Should be dict."
        return MessageId.parse(data)

    async def send(self) -> MessageId:
        res = await context.bot.send(self)
        return res.result
