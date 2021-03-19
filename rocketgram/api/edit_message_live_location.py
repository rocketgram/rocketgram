# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional

from .request import Request
from .utils import INLINE_KEYBOARDS, MessageOrBoolResultMixin


@dataclass(frozen=True)
class EditMessageLiveLocation(MessageOrBoolResultMixin, Request):
    """\
    Represents EditMessageLiveLocation request object:
    https://core.telegram.org/bots/api#editmessagelivelocation
    """

    latitude: float
    longitude: float
    chat_id: Optional[Union[int, str]] = None
    message_id: Optional[int] = None
    inline_message_id: Optional[str] = None
    horizontal_accuracy: Optional[float] = None
    heading: Optional[int] = None
    proximity_alert_radius: Optional[int] = None
    reply_markup: Optional[INLINE_KEYBOARDS] = None
