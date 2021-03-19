# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List

from .input_file import InputFile
from .request import Request
from .update_type import UpdateType
from .utils import BoolResultMixin


@dataclass(frozen=True)
class SetWebhook(BoolResultMixin, Request):
    """\
    Represents SetWebhook request object:
    https://core.telegram.org/bots/api#setwebhook
    """

    url: str
    certificate: Optional[InputFile] = None
    ip_address: Optional[str] = None
    max_connections: Optional[int] = None
    allowed_updates: Optional[List[UpdateType]] = None
    drop_pending_updates: Optional[bool] = None

    def files(self) -> List[InputFile]:
        if isinstance(self.certificate, InputFile):
            return [self.certificate]
        return list()
