# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass

from .request import Request


@dataclass(frozen=True)
class GetMe(Request):
    """\
    Represents GetMe request object:
    https://core.telegram.org/bots/api#getme
    """

    method = "getMe"
