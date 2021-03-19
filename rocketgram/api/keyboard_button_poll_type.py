# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass

from .poll_type import PollType


@dataclass(frozen=True)
class KeyboardButtonPollType:
    """\
    Represents KeyboardButtonPollType keyboard object:
    https://core.telegram.org/bots/api#keyboardbuttonpolltype
    """

    type: PollType
