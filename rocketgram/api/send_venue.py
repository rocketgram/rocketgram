# Copyright (C) 2015-2023 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional

from .request import Request
from .utils import AnyKeyboard, MessageResultMixin


@dataclass(frozen=True)
class SendVenue(MessageResultMixin, Request):
    """\
    Represents SendVenue request object:
    https://core.telegram.org/bots/api#sendvenue
    """

    chat_id: Union[int, str]
    latitude: float
    longitude: float
    title: str
    address: str
    message_thread_id: Optional[int] = None
    foursquare_id: Optional[str] = None
    foursquare_type: Optional[str] = None
    google_place_id: Optional[str] = None
    google_place_type: Optional[str] = None
    disable_notification: Optional[bool] = None
    protect_content: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    allow_sending_without_reply: Optional[bool] = None
    reply_markup: Optional[AnyKeyboard] = None
