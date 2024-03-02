# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional, List

from .input_file import InputFile
from .input_media import InputMedia
from .request import Request
from .utils import AnyInlineKeyboard, MessageOrBoolResultMixin


@dataclass(frozen=True)
class EditMessageMedia(MessageOrBoolResultMixin, Request):
    """\
    Represents EditMessageMedia request object:
    https://core.telegram.org/bots/api#editmessagemedia
    """

    media: InputMedia
    chat_id: Optional[Union[int, str]] = None
    message_id: Optional[int] = None
    inline_message_id: Optional[str] = None
    reply_markup: Optional[AnyInlineKeyboard] = None

    def files(self) -> List[InputFile]:
        out = list()
        media = self.media

        if hasattr(media, 'media') and isinstance(media.media, InputFile):
            out.append(media.media)
        if hasattr(media, 'thumbnail') and isinstance(media.thumbnail, InputFile):
            out.append(media.thumbnail)

        return out
