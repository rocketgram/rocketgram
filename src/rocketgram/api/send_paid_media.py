# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional, List

from .message_entity import MessageEntity
from .input_file import InputFile
from .input_paid_media import InputPaidMedia
from .parse_mode_type import ParseModeType
from .reply_parameters import ReplyParameters
from .request import Request
from .suggested_post_parameters import SuggestedPostParameters
from .utils import AnyKeyboard, MessageResultMixin


@dataclass(frozen=True)
class SendPaidMedia(MessageResultMixin, Request):
    """    Represents SendPaidMedia request object:
    https://core.telegram.org/bots/api#sendpaidmedia
    """

    chat_id: Union[int, str]
    star_count: int
    media: List[InputPaidMedia]
    business_connection_id: Optional[str] = None
    message_thread_id: Optional[int] = None
    direct_messages_topic_id: Optional[int] = None
    payload: Optional[str] = None
    caption: Optional[str] = None
    parse_mode: Optional[ParseModeType] = None
    caption_entities: Optional[List[MessageEntity]] = None
    show_caption_above_media: Optional[bool] = None
    disable_notification: Optional[bool] = None
    protect_content: Optional[bool] = None
    allow_paid_broadcast: Optional[bool] = None
    suggested_post_parameters: Optional[SuggestedPostParameters] = None
    reply_parameters: Optional[ReplyParameters] = None
    reply_markup: Optional[AnyKeyboard] = None

    def files(self) -> List[InputFile]:
        out = list()
        for item in self.media:
            for attribute in ('media', 'thumbnail', 'cover', 'photo'):
                value = getattr(item, attribute, None)
                if isinstance(value, InputFile):
                    out.append(value)
        return out
