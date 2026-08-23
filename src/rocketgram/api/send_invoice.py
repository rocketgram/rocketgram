# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List, Union

from .reply_parameters import ReplyParameters
from .labeled_price import LabeledPrice
from .request import Request
from .suggested_post_parameters import SuggestedPostParameters
from .utils import AnyInlineKeyboard, MessageResultMixin


@dataclass(frozen=True)
class SendInvoice(MessageResultMixin, Request):
    """\
    Represents SendInvoice request object:
    https://core.telegram.org/bots/api#sendinvoice
    """

    chat_id: Union[int, str]
    title: str
    description: str
    payload: str
    currency: str
    prices: List[LabeledPrice]
    provider_token: Optional[str] = None
    message_thread_id: Optional[int] = None
    direct_messages_topic_id: Optional[int] = None
    max_tip_amount: Optional[int] = None
    suggested_tip_amounts: Optional[List[int]] = None
    start_parameter: Optional[str] = None
    provider_data: Optional[str] = None
    photo_url: Optional[str] = None
    photo_size: Optional[int] = None
    photo_width: Optional[int] = None
    photo_height: Optional[int] = None
    need_name: Optional[bool] = None
    need_phone_number: Optional[bool] = None
    need_email: Optional[bool] = None
    need_shipping_address: Optional[bool] = None
    send_phone_number_to_provider: Optional[bool] = None
    send_email_to_provider: Optional[bool] = None
    is_flexible: Optional[bool] = None
    disable_notification: Optional[bool] = None
    protect_content: Optional[bool] = None
    message_effect_id: Optional[str] = None
    allow_paid_broadcast: Optional[bool] = None
    suggested_post_parameters: Optional[SuggestedPostParameters] = None
    reply_parameters: Optional[ReplyParameters] = None
    reply_markup: Optional[AnyInlineKeyboard] = None
