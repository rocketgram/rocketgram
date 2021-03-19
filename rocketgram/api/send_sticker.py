# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional, List

from .input_file import InputFile
from .request import Request
from .utils import ALL_KEYBOARDS, MessageResultMixin


@dataclass(frozen=True)
class SendSticker(MessageResultMixin, Request):
    """\
    Represents SendSticker request object:
    https://core.telegram.org/bots/api#sendsticker
    """

    chat_id: Union[int, str]
    sticker: Union[InputFile, str]
    disable_notification: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    allow_sending_without_reply: Optional[bool] = None
    reply_markup: Optional[ALL_KEYBOARDS] = None

    def files(self) -> List[InputFile]:
        if isinstance(self.sticker, InputFile):
            return [self.sticker]
        return list()
