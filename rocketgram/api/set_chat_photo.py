# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, List

from .input_file import InputFile
from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class SetChatPhoto(BoolResultMixin, Request):
    """\
    Represents SetChatPhoto request object:
    https://core.telegram.org/bots/api#setchatphoto
    """

    chat_id: Union[int, str]
    photo: Union[InputFile, str]

    def files(self) -> List[InputFile]:
        if isinstance(self.photo, InputFile):
            return [self.photo]
        return list()
