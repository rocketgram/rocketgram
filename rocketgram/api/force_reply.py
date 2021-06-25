# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class ForceReply:
    """\
    Represents ForceReply keyboard object:
    https://core.telegram.org/bots/api#forcereply
    """

    force_reply: bool = True
    input_field_placeholder: Optional[str] = None
    selective: Optional[bool] = None
