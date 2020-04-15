# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass


@dataclass(frozen=True)
class ForceReply:
    """\
    Represents ForceReply keyboard object:
    https://core.telegram.org/bots/api#forcereply
    """

    selective: bool = False
    force_reply: bool = True
