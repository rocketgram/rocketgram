# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, List

from .input_file import InputFile
from .request import Request


@dataclass(frozen=True)
class SetChatPhoto(Request):
    """\
    Represents SetChatPhoto request object:
    https://core.telegram.org/bots/api#setchatphoto
    """

    method = "setChatPhoto"

    chat_id: Union[int, str]
    photo: Union[InputFile, str]

    def files(self) -> List[InputFile]:
        if isinstance(self.photo, InputFile):
            return [self.photo]
        return list()
