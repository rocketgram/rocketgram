# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from typing import Optional, List

from .labeled_price import LabeledPrice
from .request import Request
from .utils import INLINE_KEYBOARDS, MessageResultMixin


class SendInvoice(MessageResultMixin, Request):
    """\
    Represents SendInvoice request object:
    https://core.telegram.org/bots/api#sendinvoice
    """

    chat_id: int
    title: str
    description: str
    payload: str
    provider_token: str
    start_parameter: str
    currency: str
    prices: List[LabeledPrice]
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
    reply_to_message_id: Optional[bool] = None
    allow_sending_without_reply: Optional[bool] = None
    reply_markup: Optional[INLINE_KEYBOARDS] = None
