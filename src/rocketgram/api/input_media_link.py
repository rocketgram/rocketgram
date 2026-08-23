# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass, field

from .input_media import InputMedia


@dataclass(frozen=True)
class InputMediaLink(InputMedia):
    """\
    Represents InputMediaLink object:
    https://core.telegram.org/bots/api#inputmedialink
    """

    type: str = field(init=False, default='link')

    url: str
