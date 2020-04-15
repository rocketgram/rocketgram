# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import List

from .passport_element_error import PassportElementError
from .request import Request


@dataclass(frozen=True)
class SetPassportDataErrors(Request):
    """\
    Represents SetPassportDataErrors request object:
    https://core.telegram.org/bots/api#setpassportdataerrors
    """

    method = "setPassportDataErrors"

    user_id: str
    errors: List[PassportElementError]
