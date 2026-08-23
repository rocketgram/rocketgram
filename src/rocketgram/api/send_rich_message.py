# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass, fields, is_dataclass
from typing import List, Optional, Union

from .input_rich_message import InputRichMessage
from .input_file import InputFile
from .request import Request
from .reply_parameters import ReplyParameters
from .suggested_post_parameters import SuggestedPostParameters
from .utils import AnyKeyboard, MessageResultMixin


@dataclass(frozen=True)
class SendRichMessage(MessageResultMixin, Request):
    """\
    Represents SendRichMessage request object:
    https://core.telegram.org/bots/api#sendrichmessage
    """

    chat_id: Union[int, str]
    rich_message: InputRichMessage
    business_connection_id: Optional[str] = None
    message_thread_id: Optional[int] = None
    direct_messages_topic_id: Optional[int] = None
    disable_notification: Optional[bool] = None
    protect_content: Optional[bool] = None
    allow_paid_broadcast: Optional[bool] = None
    message_effect_id: Optional[str] = None
    suggested_post_parameters: Optional[SuggestedPostParameters] = None
    reply_parameters: Optional[ReplyParameters] = None
    reply_markup: Optional[AnyKeyboard] = None

    def files(self) -> List[InputFile]:
        out = list()

        def collect(value):
            if isinstance(value, InputFile):
                out.append(value)
            elif is_dataclass(value):
                for item in fields(value):
                    collect(getattr(value, item.name))
            elif isinstance(value, (list, tuple)):
                for item in value:
                    collect(item)

        collect(self.rich_message)
        return out
