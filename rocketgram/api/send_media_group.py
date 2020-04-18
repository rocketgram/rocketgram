# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional, List

from .input_file import InputFile
from .input_media import InputMedia
from .request import Request
from .. import api


@dataclass(frozen=True)
class SendMediaGroup(Request):
    """\
    Represents SendMediaGroup request object:
    https://core.telegram.org/bots/api#sendmediagroup
    """

    chat_id: Union[int, str]
    media: List[InputMedia]
    disable_notification: Optional[bool] = None
    reply_to_message_id: Optional[int] = None

    def files(self) -> List[InputFile]:
        out = list()

        for e in self.media:
            if hasattr(e, 'media') and isinstance(e.media, InputFile):
                out.append(e.media)
                continue
            if hasattr(e, 'thumb') and isinstance(e.thumb, InputFile):
                out.append(e.thumb)

        return out

    def parse_result(self, data) -> List['api.Message']:
        assert isinstance(data, list), "Should be list."
        return [api.Message.parse(r) for r in data]

    async def send2(self) -> List['api.Message']:
        res = await self._send()  # noqa
        return res.result
