# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from enum import auto

from .utils import EnumAutoName


class UpdateType(EnumAutoName):
    message = auto()
    edited_message = auto()
    channel_post = auto()
    edited_channel_post = auto()
    guest_message = auto()
    message_reaction = auto()
    message_reaction_count = auto()
    inline_query = auto()
    chosen_inline_result = auto()
    callback_query = auto()
    shipping_query = auto()
    pre_checkout_query = auto()
    poll = auto()
    poll_answer = auto()
    my_chat_member = auto()
    chat_member = auto()
    chat_join_request = auto()
    business_connection = auto()
    business_message = auto()
    edited_business_message = auto()
    deleted_business_messages = auto()
    chat_boost = auto()
    removed_chat_boost = auto()
    purchased_paid_media = auto()
    subscription = auto()
    managed_bot = auto()
    unknown = auto()
