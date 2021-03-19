# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import List

from .passport_element_error import PassportElementError
from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class SetPassportDataErrors(BoolResultMixin, Request):
    """\
    Represents SetPassportDataErrors request object:
    https://core.telegram.org/bots/api#setpassportdataerrors
    """

    user_id: str
    errors: List[PassportElementError]
