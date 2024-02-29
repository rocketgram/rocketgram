# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional, List

from . import reply_parameters
from .input_file import InputFile
from .request import Request
from .utils import AnyKeyboard, MessageResultMixin


@dataclass(frozen=True)
class SendSticker(MessageResultMixin, Request):
    """\
    Represents SendSticker request object:
    https://core.telegram.org/bots/api#sendsticker
    """

    chat_id: Union[int, str]
    sticker: Union[InputFile, str]
    message_thread_id: Optional[int] = None
    emoji: Optional[str] = None
    disable_notification: Optional[bool] = None
    protect_content: Optional[bool] = None
    reply_parameters: Optional['reply_parameters.ReplyParameters'] = None
    reply_markup: Optional[AnyKeyboard] = None

    def files(self) -> List[InputFile]:
        if isinstance(self.sticker, InputFile):
            return [self.sticker]
        return list()
