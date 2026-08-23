# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, Union

from .input_media import InputMedia
from .request import Request
from .utils import AnyInlineKeyboard, BoolResultMixin


@dataclass(frozen=True)
class EditEphemeralMessageMedia(BoolResultMixin, Request):
    """\
    Represents EditEphemeralMessageMedia request object:
    https://core.telegram.org/bots/api#editephemeralmessagemedia
    """

    chat_id: Union[int, str]
    receiver_user_id: int
    ephemeral_message_id: int
    media: InputMedia
    reply_markup: Optional[AnyInlineKeyboard] = None
