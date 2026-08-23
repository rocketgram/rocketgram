# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass

from .input_rich_message import InputRichMessage


@dataclass(frozen=True)
class InputRichMessageContent:
    """\
    Represents InputRichMessageContent object:
    https://core.telegram.org/bots/api#inputrichmessagecontent
    """

    rich_message: InputRichMessage
