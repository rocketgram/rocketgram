# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .input_rich_message import InputRichMessage
from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class SendRichMessageDraft(BoolResultMixin, Request):
    """\
    Represents SendRichMessageDraft request object:
    https://core.telegram.org/bots/api#sendrichmessagedraft
    """

    chat_id: int
    draft_id: int
    rich_message: InputRichMessage
    message_thread_id: Optional[int] = None
