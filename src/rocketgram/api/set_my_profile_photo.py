# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import List

from .input_file import InputFile
from .input_profile_photo import InputProfilePhoto
from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class SetMyProfilePhoto(BoolResultMixin, Request):
    """\
    Represents SetMyProfilePhoto request object:
    https://core.telegram.org/bots/api#setmyprofilephoto
    """

    photo: InputProfilePhoto

    def files(self) -> List[InputFile]:
        for attribute in ('photo', 'animation'):
            value = getattr(self.photo, attribute, None)
            if isinstance(value, InputFile):
                return [value]
        return []
