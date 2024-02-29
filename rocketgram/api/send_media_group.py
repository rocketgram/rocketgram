# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional, List

from . import reply_parameters
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
    media: List[InputMedia]
    message_thread_id: Optional[int] = None
    disable_notification: Optional[bool] = None
    protect_content: Optional[bool] = None
    reply_parameters: Optional['reply_parameters.ReplyParameters'] = None

    def files(self) -> List[InputFile]:
        out = list()

        for e in self.media:
            if hasattr(e, 'media') and isinstance(e.media, InputFile):
                out.append(e.media)
                continue
            if hasattr(e, 'thumbnail') and isinstance(e.thumbnail, InputFile):
                out.append(e.thumbnail)

        return out

    def parse_result(self, data) -> List['api.Message']:
        assert isinstance(data, list), "Should be list."
        return [api.Message.parse(r) for r in data]

    async def send(self) -> List['api.Message']:
        res = await context.bot.send(self)
        return res.result
