# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from contextvars import ContextVar
from typing import List, Optional, TYPE_CHECKING

from . import api

if TYPE_CHECKING:
    from .executors import Executor
    from .bot import Bot

current_executor = ContextVar('current_executor')
current_bot = ContextVar('current_bot')
current_webhook_requests = ContextVar('current_webhook_requests')

current_update = ContextVar('current_update')
current_message = ContextVar('current_message')
current_callback = ContextVar('current_callback')
current_inline = ContextVar('current_inline')
current_result = ContextVar('current_result')
current_shipping = ContextVar('current_shipping')
current_checkout = ContextVar('current_checkout')
current_poll = ContextVar('current_poll')
current_answer = ContextVar('current_answer')
current_member = ContextVar('current_member')

current_chat = ContextVar('current_chat')
current_user = ContextVar('current_user')


class Context:
    __instance: 'Context' = None
    __slots__ = tuple()

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

        return current_executor.get(None)

    @executor.setter
    def executor(self, executor: 'Executor'):
        current_executor.set(executor)

    @property
    def bot(self) -> Optional['Bot']:
        """Returns current Bot object."""

        return current_bot.get(None)

    @bot.setter
    def bot(self, bot: 'Bot'):
        current_bot.set(bot)

    @property
    def update(self) -> Optional['api.Update']:
        """Returns Update object for current request."""

        return current_update.get(None)

    @update.setter
    def update(self, update: 'api.Update'):
        current_update.set(update)

    @property
    def message(self) -> Optional['api.Message']:
        """Returns Message object for current request."""

        return current_message.get(None)

    @message.setter
    def message(self, update: 'api.Message'):
        current_message.set(update)

    @property
    def chat(self) -> Optional['api.Chat']:
        """Returns Chat object for current request."""

        return current_chat.get(None)

    @chat.setter
    def chat(self, chat: 'api.Chat'):
        current_chat.set(chat)

    @property
    def user(self) -> Optional['api.User']:
        """Returns User object for current request."""

        return current_user.get(None)

    @user.setter
    def user(self, user: 'api.User'):
        current_user.set(user)

    @property
    def callback(self) -> Optional['api.CallbackQuery']:
        """Returns CallbackQuery object for current request."""

        return current_callback.get(None)

    @callback.setter
    def callback(self, callback: 'api.CallbackQuery'):
        current_callback.set(callback)

    @property
    def inline(self) -> Optional['api.InlineQuery']:
        """Returns InlineQuery object for current request."""

        return current_inline.get(None)

    @inline.setter
    def inline(self, inline: 'api.InlineQuery'):
        current_inline.set(inline)

    @property
    def result(self) -> Optional['api.ChosenInlineResult']:
        """Returns ChosenInlineResult object for current request."""

        return current_result.get(None)

    @result.setter
    def result(self, result: 'api.ChosenInlineResult'):
        current_result.set(result)

    @property
    def shipping(self) -> Optional['api.ShippingQuery']:
        """Returns ShippingQuery object for current request."""

        return current_shipping.get(None)

    @shipping.setter
    def shipping(self, shipping: 'api.ShippingQuery'):
        current_shipping.set(shipping)

    @property
    def checkout(self) -> Optional['api.PreCheckoutQuery']:
        """Returns PreCheckoutQuery object for current request."""

        return current_checkout.get(None)

    @checkout.setter
    def checkout(self, checkout: 'api.PreCheckoutQuery'):
        current_checkout.set(checkout)

    @property
    def poll(self) -> Optional['api.Poll']:
        """Returns Poll object for current request."""

        return current_poll.get(None)

    @poll.setter
    def poll(self, poll: 'api.Poll'):
        current_poll.set(poll)

    @property
    def answer(self) -> Optional['api.PollAnswer']:
        """Returns PollAnswer object for current request."""

        return current_answer.get(None)

    @answer.setter
    def answer(self, answer: 'api.PollAnswer'):
        current_answer.set(answer)

    @property
    def member(self) -> Optional['api.ChatMemberUpdated']:
        """Returns ChatMemberUpdated object for current request."""

        return current_member.get(None)

    @member.setter
    def member(self, member: 'api.ChatMemberUpdated'):
        current_member.set(member)

    @staticmethod
    def webhook(request: 'api.Request'):
        """Sets Request object to be sent through webhook-request mechanism."""

        current_webhook_requests.get().append(request)

    @property
    def webhook_requests(self) -> List['api.Request']:
        """Returns list of current requests awaits sent through webhook-request mechanism."""

        return current_webhook_requests.get()

    @webhook_requests.setter
    def webhook_requests(self, webhook_requests):
        """Returns list of current requests awaits sent through webhook-request mechanism."""

        current_webhook_requests.set(webhook_requests)

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


context = Context.instance()
