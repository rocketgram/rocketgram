# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .input_message_content import InputMessageContent


@dataclass(frozen=True)
class InputContactMessageContent(InputMessageContent):
    """\
    Represents InputContactMessageContent object:
    https://core.telegram.org/bots/api#inputcontactmessagecontent
    """

    latitude: float
    longitude: float
    title: str
    address: str
    foursquare_id: Optional[str] = None
    foursquare_type: Optional[str] = None
