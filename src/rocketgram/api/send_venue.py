# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional

from . import reply_parameters
from .request import Request
from .suggested_post_parameters import SuggestedPostParameters
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
    business_connection_id: Optional[str] = None
    message_thread_id: Optional[int] = None
    direct_messages_topic_id: Optional[int] = None
    receiver_user_id: Optional[int] = None
    callback_query_id: Optional[str] = None
    foursquare_id: Optional[str] = None
    foursquare_type: Optional[str] = None
    google_place_id: Optional[str] = None
    google_place_type: Optional[str] = None
    disable_notification: Optional[bool] = None
    protect_content: Optional[bool] = None
    message_effect_id: Optional[str] = None
    allow_paid_broadcast: Optional[bool] = None
    suggested_post_parameters: Optional[SuggestedPostParameters] = None
    reply_parameters: Optional['reply_parameters.ReplyParameters'] = None
    reply_markup: Optional[AnyKeyboard] = None
