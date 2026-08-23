# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional

from .request import Request
from .suggested_post_parameters import SuggestedPostParameters
from .utils import MessageResultMixin


@dataclass(frozen=True)
class ForwardMessage(MessageResultMixin, Request):
    """\
    Represents ForwardMessage request object:
    https://core.telegram.org/bots/api#forwardmessage
    """

    chat_id: Union[int, str]
    from_chat_id: Union[int, str]
    message_id: int
    message_thread_id: Optional[int] = None
    direct_messages_topic_id: Optional[int] = None
    video_start_timestamp: Optional[int] = None
    disable_notification: Optional[bool] = None
    protect_content: Optional[bool] = None
    message_effect_id: Optional[str] = None
    suggested_post_parameters: Optional[SuggestedPostParameters] = None
