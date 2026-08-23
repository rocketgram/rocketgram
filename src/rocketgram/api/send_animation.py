# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional, List

from . import reply_parameters
from .input_file import InputFile
from .message_entity import MessageEntity
from .parse_mode_type import ParseModeType
from .request import Request
from .suggested_post_parameters import SuggestedPostParameters
from .utils import AnyKeyboard, MessageResultMixin


@dataclass(frozen=True)
class SendAnimation(MessageResultMixin, Request):
    """\
    Represents SendAnimation request object:
    https://core.telegram.org/bots/api#sendanimation
    """

    chat_id: Union[int, str]
    animation: Union[InputFile, str]
    business_connection_id: Optional[str] = None
    message_thread_id: Optional[int] = None
    direct_messages_topic_id: Optional[int] = None
    receiver_user_id: Optional[int] = None
    callback_query_id: Optional[str] = None
    duration: Optional[int] = None
    width: Optional[int] = None
    height: Optional[int] = None
    thumbnail: Optional[Union[InputFile, str]] = None
    caption: Optional[str] = None
    parse_mode: Optional[ParseModeType] = None
    caption_entities: Optional[List[MessageEntity]] = None
    show_caption_above_media: Optional[bool] = None
    has_spoiler: Optional[bool] = None
    disable_notification: Optional[bool] = None
    protect_content: Optional[bool] = None
    message_effect_id: Optional[str] = None
    allow_paid_broadcast: Optional[bool] = None
    suggested_post_parameters: Optional[SuggestedPostParameters] = None
    reply_parameters: Optional['reply_parameters.ReplyParameters'] = None
    reply_markup: Optional[AnyKeyboard] = None

    def files(self) -> List[InputFile]:
        out = list()
        if isinstance(self.animation, InputFile):
            out.append(self.animation)
        if isinstance(self.thumbnail, InputFile):
            out.append(self.thumbnail)
        return out
