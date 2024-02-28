# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from contextvars import ContextVar
from typing import List, Optional, TYPE_CHECKING

from . import api

if TYPE_CHECKING:
    from .executors import Executor
    from .bot import Bot

_current_executor = ContextVar('current_executor')
_current_bot = ContextVar('current_bot')
_current_webhook_requests = ContextVar('current_webhook_requests')

_current_update = ContextVar('current_update')
_current_message = ContextVar('current_message')
_current_callback = ContextVar('current_callback')
_current_inline = ContextVar('current_inline')
_current_result = ContextVar('current_result')
_current_shipping = ContextVar('current_shipping')
_current_checkout = ContextVar('current_checkout')
_current_poll = ContextVar('current_poll')
_current_answer = ContextVar('current_answer')
_current_member = ContextVar('current_member')

_current_reaction = ContextVar('current_reaction')
_current_reaction_count = ContextVar('current_reaction_count')
_current_boost = ContextVar('current_boost')
_current_removed_boost = ContextVar('current_removed_boost')

_current_chat = ContextVar('current_chat')
_current_user = ContextVar('current_user')


class Context:
    __instance: 'Context' = None
    __slots__ = ()

    def __new__(cls):
        if Context.__instance is None:
            Context.__instance = super().__new__(cls)
        return Context.__instance

    @classmethod
    def instance(cls) -> 'Context':
        return cls()

    @property
    def executor(self) -> Optional['Executor']:
        """Returns Executor object for current request."""

        return _current_executor.get(None)

    @executor.setter
    def executor(self, executor: 'Executor'):
        _current_executor.set(executor)

    @property
    def bot(self) -> Optional['Bot']:
        """Returns current Bot object."""

        return _current_bot.get(None)

    @bot.setter
    def bot(self, bot: 'Bot'):
        _current_bot.set(bot)

    @property
    def update(self) -> Optional['api.Update']:
        """Returns Update object for current request."""

        return _current_update.get(None)

    @update.setter
    def update(self, update: 'api.Update'):
        _current_update.set(update)

    @property
    def message(self) -> Optional['api.Message']:
        """Returns Message object for current request."""

        return _current_message.get(None)

    @message.setter
    def message(self, update: 'api.Message'):
        _current_message.set(update)

    @property
    def chat(self) -> Optional['api.Chat']:
        """Returns Chat object for current request."""

        return _current_chat.get(None)

    @chat.setter
    def chat(self, chat: 'api.Chat'):
        _current_chat.set(chat)

    @property
    def user(self) -> Optional['api.User']:
        """Returns User object for current request."""

        return _current_user.get(None)

    @user.setter
    def user(self, user: 'api.User'):
        _current_user.set(user)

    @property
    def callback(self) -> Optional['api.CallbackQuery']:
        """Returns CallbackQuery object for current request."""

        return _current_callback.get(None)

    @callback.setter
    def callback(self, callback: 'api.CallbackQuery'):
        _current_callback.set(callback)

    @property
    def inline(self) -> Optional['api.InlineQuery']:
        """Returns InlineQuery object for current request."""

        return _current_inline.get(None)

    @inline.setter
    def inline(self, inline: 'api.InlineQuery'):
        _current_inline.set(inline)

    @property
    def result(self) -> Optional['api.ChosenInlineResult']:
        """Returns ChosenInlineResult object for current request."""

        return _current_result.get(None)

    @result.setter
    def result(self, result: 'api.ChosenInlineResult'):
        _current_result.set(result)

    @property
    def shipping(self) -> Optional['api.ShippingQuery']:
        """Returns ShippingQuery object for current request."""

        return _current_shipping.get(None)

    @shipping.setter
    def shipping(self, shipping: 'api.ShippingQuery'):
        _current_shipping.set(shipping)

    @property
    def checkout(self) -> Optional['api.PreCheckoutQuery']:
        """Returns PreCheckoutQuery object for current request."""

        return _current_checkout.get(None)

    @checkout.setter
    def checkout(self, checkout: 'api.PreCheckoutQuery'):
        _current_checkout.set(checkout)

    @property
    def poll(self) -> Optional['api.Poll']:
        """Returns Poll object for current request."""

        return _current_poll.get(None)

    @poll.setter
    def poll(self, poll: 'api.Poll'):
        _current_poll.set(poll)

    @property
    def answer(self) -> Optional['api.PollAnswer']:
        """Returns PollAnswer object for current request."""

        return _current_answer.get(None)

    @answer.setter
    def answer(self, answer: 'api.PollAnswer'):
        _current_answer.set(answer)

    @property
    def member(self) -> Optional['api.ChatMemberUpdated']:
        """Returns ChatMemberUpdated object for current request."""

        return _current_member.get(None)

    @member.setter
    def member(self, member: 'api.ChatMemberUpdated'):
        _current_member.set(member)

    @property
    def reaction(self) -> Optional['api.MessageReactionUpdated']:
        """Returns MessageReaction object for current request."""

        return _current_reaction.get(None)

    @reaction.setter
    def reaction(self, reaction: 'api.MessageReactionUpdated'):
        _current_reaction.set(reaction)

    @property
    def reaction_count(self) -> Optional['api.MessageReactionCountUpdated']:
        """Returns MessageReactionCount object for current request."""

        return _current_reaction_count.get(None)

    @reaction_count.setter
    def reaction_count(self, reaction_count: 'api.MessageReactionCountUpdated'):
        _current_reaction_count.set(reaction_count)

    @property
    def boost(self) -> Optional['api.ChatBoostUpdated']:
        """Returns ChatBoostUpdated object for current request."""

        return _current_boost.get(None)

    @boost.setter
    def boost(self, boost: 'api.ChatBoostUpdated'):
        _current_boost.set(boost)

    @property
    def removed_boost(self) -> Optional['api.ChatBoostRemoved']:
        """Returns ChatBoostRemoved object for current request."""

        return _current_removed_boost.get(None)

    @removed_boost.setter
    def removed_boost(self, removed_boost: 'api.ChatBoostRemoved'):
        _current_removed_boost.set(removed_boost)

    @staticmethod
    def webhook(request: 'api.Request'):
        """Sets the Request object to be sent through the webhook-request mechanism."""

        _current_webhook_requests.get().append(request)

    @property
    def webhook_requests(self) -> List['api.Request']:
        """Returns list of current requests that awaits sent through webhook-request mechanism."""

        return _current_webhook_requests.get()

    @webhook_requests.setter
    def webhook_requests(self, webhook_requests):
        """Returns list of current requests that awaits sent through webhook-request mechanism."""

        _current_webhook_requests.set(webhook_requests)

    def assign(self, executor: 'Executor', bot: 'Bot', update: 'api.Update'):

        self.executor = executor
        self.bot = bot

        self.webhook_requests = list()

        self.update = update

        self.message = None
        self.callback = None
        self.shipping = None
        self.inline = None
        self.result = None
        self.checkout = None
        self.poll = None
        self.answer = None
        self.member = None

        self.reaction = None
        self.reaction_count = None
        self.boost = None
        self.removed_boost = None

        self.chat = None
        self.user = None

        if update.type is api.UpdateType.message:
            self.message = update.message
            self.chat = update.message.chat
            self.user = update.message.user
        elif update.type is api.UpdateType.edited_message:
            self.message = update.edited_message
            self.chat = update.edited_message.chat
            self.user = update.edited_message.user
        elif update.type is api.UpdateType.channel_post:
            self.message = update.channel_post
            self.chat = update.channel_post.chat
            self.user = update.channel_post.user
        elif update.type is api.UpdateType.edited_channel_post:
            self.message = update.edited_channel_post
            self.chat = update.edited_channel_post.chat
            self.user = update.edited_channel_post.user
        elif update.type is api.UpdateType.message_reaction:
            self.reaction = update.message_reaction
            self.chat = update.message_reaction.chat
            self.user = update.message_reaction.user
        elif update.type is api.UpdateType.message_reaction_count:
            self.reaction_count = update.message_reaction_count
            self.chat = update.message_reaction_count.chat
        elif update.type is api.UpdateType.inline_query:
            self.inline = update.inline_query
            self.user = update.inline_query.user
        elif update.type is api.UpdateType.chosen_inline_result:
            self.result = update.chosen_inline_result
            self.user = update.chosen_inline_result.user
        elif update.type is api.UpdateType.callback_query:
            self.callback = update.callback_query
            self.message = update.callback_query.message
            if update.callback_query.message:
                self.chat = update.callback_query.message.chat
            self.user = update.callback_query.user
        elif update.type is api.UpdateType.shipping_query:
            self.shipping = update.shipping_query
            self.user = update.shipping_query.user
        elif update.type is api.UpdateType.pre_checkout_query:
            self.checkout = update.pre_checkout_query
            self.user = update.pre_checkout_query.user
        elif update.type is api.UpdateType.poll:
            self.poll = update.poll
        elif update.type is api.UpdateType.poll_answer:
            self.answer = update.poll_answer
            self.user = update.poll_answer.user
        elif update.type is api.UpdateType.my_chat_member:
            self.member = update.my_chat_member
            self.chat = update.my_chat_member.chat
            self.user = update.my_chat_member.user
        elif update.type is api.UpdateType.chat_member:
            self.member = update.chat_member
            self.chat = update.chat_member.chat
            self.user = update.chat_member.user
        elif update.type is api.UpdateType.chat_boost:
            self.boost = update.chat_boost
            self.chat = update.chat_boost.chat
        elif update.type is api.UpdateType.removed_chat_boost:
            self.removed_boost = update.removed_chat_boost
            self.chat = update.removed_chat_boost.chat


context: Context = Context.instance()
