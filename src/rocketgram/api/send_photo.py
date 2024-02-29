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
from .utils import AnyKeyboard, MessageResultMixin


@dataclass(frozen=True)
class SendPhoto(MessageResultMixin, Request):
    """\
    Represents SendPhoto request object:
    https://core.telegram.org/bots/api#sendphoto
    """

    chat_id: Union[int, str]
    photo: Union[InputFile, str]
    message_thread_id: Optional[int] = None
    caption: Optional[str] = None
    parse_mode: Optional[ParseModeType] = None
    caption_entities: Optional[List[MessageEntity]] = None
    has_spoiler: Optional[bool] = None
    disable_notification: Optional[bool] = None
    protect_content: Optional[bool] = None
    reply_parameters: Optional['reply_parameters.ReplyParameters'] = None
    reply_markup: Optional[AnyKeyboard] = None

    def files(self) -> List[InputFile]:
        if isinstance(self.photo, InputFile):
            return [self.photo]
        return list()
