# Copyright (C) 2015-2023 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional, Tuple

from .input_file import InputFile
from .input_media import InputMedia
from .request import Request
from .. import api
from ..context import context


@dataclass(frozen=True)
class SendMediaGroup(Request):
    """\
    Represents SendMediaGroup request object:
    https://core.telegram.org/bots/api#sendmediagroup
    """

    chat_id: Union[int, str]
    media: Tuple[InputMedia, ...]
    message_thread_id: Optional[int] = None
    disable_notification: Optional[bool] = None
    protect_content: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    allow_sending_without_reply: Optional[bool] = None

    def files(self) -> Tuple[InputFile, ...]:
        out = list()

        for e in self.media:
            if hasattr(e, 'media') and isinstance(e.media, InputFile):
                out.append(e.media)
                continue
            if hasattr(e, 'thumbnail') and isinstance(e.thumbnail, InputFile):
                out.append(e.thumbnail)

        return tuple(out)

    def parse_result(self, data) -> Tuple['api.Message', ...]:
        assert isinstance(data, list), "Should be list."
        return tuple(api.Message.parse(r) for r in data)

    async def send(self) -> Tuple['api.Message', ...]:
        res = await context.bot.send(self)
        return res.result
