# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional, List

from .input_file import InputFile
from .parse_mode_type import ParseModeType
from .request import Request
from .utils import ALL_KEYBOARDS, MessageResultMixin


@dataclass(frozen=True)
class SendAnimation(MessageResultMixin, Request):
    """\
    Represents SendAnimation request object:
    https://core.telegram.org/bots/api#sendanimation
    """

    chat_id: Union[int, str]
    animation: Union[InputFile, str]
    duration: Optional[int] = None
    width: Optional[int] = None
    height: Optional[int] = None
    thumb: Optional[Union[InputFile, str]] = None
    caption: Optional[str] = None
    parse_mode: Optional[ParseModeType] = None
    disable_notification: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    reply_markup: Optional[ALL_KEYBOARDS] = None

    def files(self) -> List[InputFile]:
        out = list()
        if isinstance(self.animation, InputFile):
            out.append(self.animation)
        if isinstance(self.thumb, InputFile):
            out.append(self.thumb)
        return out
