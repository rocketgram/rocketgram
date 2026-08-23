# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Dict, Optional

from .business_connection import BusinessConnection
from .business_messages_deleted import BusinessMessagesDeleted
from .bot_subscription_updated import BotSubscriptionUpdated
from .callback_query import CallbackQuery
from .chat_boost_removed import ChatBoostRemoved
from .chat_boost_updated import ChatBoostUpdated
from .chat_join_request import ChatJoinRequest
from .chat_member_updated import ChatMemberUpdated
from .chosen_inline_result import ChosenInlineResult
from .inline_query import InlineQuery
from .message import Message
from .message_reaction_count_updated import MessageReactionCountUpdated
from .message_reaction_updated import MessageReactionUpdated
from .managed_bot_updated import ManagedBotUpdated
from .paid_media_purchased import PaidMediaPurchased
from .poll import Poll
from .poll_answer import PollAnswer
from .pre_checkout_query import PreCheckoutQuery
from .shipping_query import ShippingQuery
from .update_type import UpdateType


@dataclass(frozen=True)
class Update:
    """\
    Represents Update object:
    https://core.telegram.org/bots/api#update

    Additional fields:
    raw
    type
    """

    raw: Dict
    update_id: int
    type: UpdateType
    message: Optional[Message]
    edited_message: Optional[Message]
    channel_post: Optional[Message]
    edited_channel_post: Optional[Message]
    guest_message: Optional[Message]
    business_connection: Optional[BusinessConnection]
    business_message: Optional[Message]
    edited_business_message: Optional[Message]
    deleted_business_messages: Optional[BusinessMessagesDeleted]
    message_reaction: Optional[MessageReactionUpdated]
    message_reaction_count: Optional[MessageReactionCountUpdated]
    inline_query: Optional[InlineQuery]
    chosen_inline_result: Optional[ChosenInlineResult]
    callback_query: Optional[CallbackQuery]
    shipping_query: Optional[ShippingQuery]
    pre_checkout_query: Optional[PreCheckoutQuery]
    poll: Optional[Poll]
    poll_answer: Optional[PollAnswer]
    my_chat_member: Optional[ChatMemberUpdated]
    chat_member: Optional[ChatMemberUpdated]
    chat_join_request: Optional[ChatJoinRequest]
    chat_boost: Optional[ChatBoostUpdated]
    removed_chat_boost: Optional[ChatBoostRemoved]
    purchased_paid_media: Optional[PaidMediaPurchased]
    subscription: Optional[BotSubscriptionUpdated]
    managed_bot: Optional[ManagedBotUpdated]

    @classmethod
    def parse(cls, data: Dict) -> 'Update':
        message = Message.parse(data.get('message'))
        edited_message = Message.parse(data.get('edited_message'))
        channel_post = Message.parse(data.get('channel_post'))
        edited_channel_post = Message.parse(data.get('edited_channel_post'))
        guest_message = Message.parse(data.get('guest_message'))
        business_connection = BusinessConnection.parse(data.get('business_connection'))
        business_message = Message.parse(data.get('business_message'))
        edited_business_message = Message.parse(data.get('edited_business_message'))
        deleted_business_messages = BusinessMessagesDeleted.parse(data.get('deleted_business_messages'))
        message_reaction = MessageReactionUpdated.parse(data.get('message_reaction'))
        message_reaction_count = MessageReactionCountUpdated.parse(data.get('message_reaction_count'))
        inline_query = InlineQuery.parse(data.get('inline_query'))
        chosen_inline_result = ChosenInlineResult.parse(data.get('chosen_inline_result'))
        callback_query = CallbackQuery.parse(data.get('callback_query'))
        shipping_query = ShippingQuery.parse(data.get('shipping_query'))
        pre_checkout_query = PreCheckoutQuery.parse(data.get('pre_checkout_query'))
        poll = Poll.parse(data.get('poll'))
        poll_answer = PollAnswer.parse(data.get('poll_answer'))
        my_chat_member = ChatMemberUpdated.parse(data.get('my_chat_member'))
        chat_member = ChatMemberUpdated.parse(data.get('chat_member'))
        chat_join_request = ChatJoinRequest.parse(data.get('chat_join_request'))
        chat_boost = ChatBoostUpdated.parse(data.get('chat_boost'))
        removed_chat_boost = ChatBoostRemoved.parse(data.get('removed_chat_boost'))
        purchased_paid_media = PaidMediaPurchased.parse(data.get('purchased_paid_media'))
        subscription = BotSubscriptionUpdated.parse(data.get('subscription'))
        managed_bot = ManagedBotUpdated.parse(data.get('managed_bot'))

        update_type = UpdateType.unknown
        if message:
            update_type = UpdateType.message
        elif edited_message:
            update_type = UpdateType.edited_message
        elif channel_post:
            update_type = UpdateType.channel_post
        elif edited_channel_post:
            update_type = UpdateType.edited_channel_post
        elif guest_message:
            update_type = UpdateType.guest_message
        elif business_connection:
            update_type = UpdateType.business_connection
        elif business_message:
            update_type = UpdateType.business_message
        elif edited_business_message:
            update_type = UpdateType.edited_business_message
        elif deleted_business_messages:
            update_type = UpdateType.deleted_business_messages
        elif message_reaction:
            update_type = UpdateType.message_reaction
        elif message_reaction_count:
            update_type = UpdateType.message_reaction_count
        elif inline_query:
            update_type = UpdateType.inline_query
        elif chosen_inline_result:
            update_type = UpdateType.chosen_inline_result
        elif callback_query:
            update_type = UpdateType.callback_query
        elif shipping_query:
            update_type = UpdateType.shipping_query
        elif pre_checkout_query:
            update_type = UpdateType.pre_checkout_query
        elif poll:
            update_type = UpdateType.poll
        elif poll_answer:
            update_type = UpdateType.poll_answer
        elif my_chat_member:
            update_type = UpdateType.my_chat_member
        elif chat_member:
            update_type = UpdateType.chat_member
        elif chat_join_request:
            update_type = UpdateType.chat_join_request
        elif chat_boost:
            update_type = UpdateType.chat_boost
        elif removed_chat_boost:
            update_type = UpdateType.removed_chat_boost
        elif purchased_paid_media:
            update_type = UpdateType.purchased_paid_media
        elif subscription:
            update_type = UpdateType.subscription
        elif managed_bot:
            update_type = UpdateType.managed_bot

        return cls(
            data,
            data['update_id'],
            update_type,
            message,
            edited_message,
            channel_post,
            edited_channel_post,
            guest_message,
            business_connection,
            business_message,
            edited_business_message,
            deleted_business_messages,
            message_reaction,
            message_reaction_count,
            inline_query,
            chosen_inline_result,
            callback_query,
            shipping_query,
            pre_checkout_query,
            poll,
            poll_answer,
            my_chat_member,
            chat_member,
            chat_join_request,
            chat_boost,
            removed_chat_boost,
            purchased_paid_media,
            subscription,
            managed_bot,
        )
