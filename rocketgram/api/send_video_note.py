# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional, List

from .input_file import InputFile
from .request import Request
from .utils import ALL_KEYBOARDS, MessageResultMixin


@dataclass(frozen=True)
class SendVideoNote(MessageResultMixin, Request):
    """\
    Represents SendVideoNote request object:
    https://core.telegram.org/bots/api#sendvideonote
    """

    chat_id: Union[int, str]
    video_note: Union[InputFile, str]
    message_thread_id: Optional[int] = None
    duration: Optional[int] = None
    length: Optional[int] = None
    thumbnail: Union[InputFile, str] = None
    disable_notification: Optional[bool] = None
    protect_content: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    allow_sending_without_reply: Optional[bool] = None
    reply_markup: Optional[ALL_KEYBOARDS] = None

    def files(self) -> List[InputFile]:
        out = list()
        if isinstance(self.video_note, InputFile):
            out.append(self.video_note)
        if isinstance(self.thumbnail, InputFile):
            out.append(self.thumbnail)
        return out
