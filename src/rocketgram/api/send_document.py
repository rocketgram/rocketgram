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
class SendDocument(MessageResultMixin, Request):
    """\
    Represents SendDocument request object:
    https://core.telegram.org/bots/api#senddocument
    """

    chat_id: Union[int, str]
    document: Union[InputFile, str]
    message_thread_id: Optional[int] = None
    thumbnail: Optional[Union[InputFile, str]] = None
    caption: Optional[str] = None
    parse_mode: Optional[ParseModeType] = None
    caption_entities: Optional[List[MessageEntity]] = None
    disable_content_type_detection: Optional[bool] = None
    disable_notification: Optional[bool] = None
    protect_content: Optional[bool] = None
    reply_parameters: Optional['reply_parameters.ReplyParameters'] = None
    reply_markup: Optional[AnyKeyboard] = None

    def files(self) -> List[InputFile]:
        out = list()
        if isinstance(self.document, InputFile):
            out.append(self.document)
        if isinstance(self.thumbnail, InputFile):
            out.append(self.thumbnail)
        return out
