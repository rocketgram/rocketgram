# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional, List

from .input_file import InputFile
from .parse_mode_type import ParseModeType
from .request import Request
from .utils import ALL_KEYBOARDS


@dataclass(frozen=True)
class SendVoice(Request):
    """\
    Represents SendVoice request object:
    https://core.telegram.org/bots/api#sendvoice
    """

    method = "sendVoice"

    chat_id: Union[int, str]
    voice: Union[InputFile, str]
    duration: Optional[int] = None
    caption: Optional[str] = None
    parse_mode: Optional[ParseModeType] = None
    disable_notification: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    reply_markup: Optional[ALL_KEYBOARDS] = None

    def files(self) -> List[InputFile]:
        if isinstance(self.voice, InputFile):
            return [self.voice]
        return list()
