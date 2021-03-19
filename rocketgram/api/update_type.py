# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from enum import auto

from .utils import EnumAutoName


class UpdateType(EnumAutoName):
    message = auto()
    edited_message = auto()
    channel_post = auto()
    edited_channel_post = auto()
    inline_query = auto()
    chosen_inline_result = auto()
    callback_query = auto()
    shipping_query = auto()
    pre_checkout_query = auto()
    poll = auto()
    poll_answer = auto()
    my_chat_member = auto()
    chat_member = auto()
    unknown = auto()
