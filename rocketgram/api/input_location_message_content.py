# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .input_message_content import InputMessageContent


@dataclass(frozen=True)
class InputLocationMessageContent(InputMessageContent):
    """\
    Represents InputLocationMessageContent object:
    https://core.telegram.org/bots/api#inputlocationmessagecontent
    """

    latitude: float
    longitude: float
    horizontal_accuracy: Optional[float] = None
    live_period: Optional[int] = None
    heading: Optional[int] = None
    proximity_alert_radius: Optional[int] = None
