# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass

from .request import Request
from .utils import FileResultMixin


@dataclass(frozen=True)
class GetFile(FileResultMixin, Request):
    """\
    Represents GetFile request object:
    https://core.telegram.org/bots/api#getfile
    """

    file_id: str
