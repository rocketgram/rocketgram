# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).

import logging
from contextvars import ContextVar
from typing import List, Optional, TYPE_CHECKING
from . import api

if TYPE_CHECKING:
    from . import bot, executors

current_executor = ContextVar('current_executor')
current_bot = ContextVar('current_bot')
current_webhook_requests = ContextVar('current_webhook_requests')

current_update = ContextVar('current_update')
current_message = ContextVar('current_message')
current_callback = ContextVar('current_callback')
current_chat = ContextVar('current_chat')
current_user = ContextVar('current_user')

logger = logging.getLogger('rocketgram.context')


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
    def executor(self) -> Optional['executors.Executor']:
        """Returns Executor object for current request."""

        return current_executor.get(None)

    @executor.setter
    def executor(self, executor: 'executors.Executor'):
        current_executor.set(executor)

    @property
    def bot(self) -> Optional['bot.Bot']:
        """Returns current Bot object."""

        return current_bot.get(None)

    @bot.setter
    def bot(self, bot: 'bot.Bot'):
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
    def callback(self, user: 'api.CallbackQuery'):
        current_callback.set(user)

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

    def assign(self, executor: 'executors.Executor', bot: 'bot.Bot', update: 'api.Update'):

        self.executor = executor
        self.bot = bot

        self.webhook_requests = list()

        self.update = update
        self.message = None
        self.chat = None
        self.user = None

        if update.update_type is api.UpdateType.message:
            self.message = update.message
            self.chat = update.message.chat
            self.user = update.message.user
        elif update.update_type is api.UpdateType.edited_message:
            self.message = update.edited_message
            self.chat = update.edited_message.chat
            self.user = update.edited_message.user
        elif update.update_type is api.UpdateType.channel_post:
            self.message = update.channel_post
            self.chat = update.channel_post.chat
            self.user = update.channel_post.user
        elif update.update_type is api.UpdateType.edited_channel_post:
            self.message = update.edited_channel_post
            self.chat = update.edited_channel_post.chat
            self.user = update.edited_channel_post.user
        elif update.update_type is api.UpdateType.inline_query:
            self.user = update.inline_query.user
        elif update.update_type is api.UpdateType.chosen_inline_result:
            self.user = update.chosen_inline_result.user
        elif update.update_type is api.UpdateType.callback_query:
            self.callback = update.callback_query
            self.message = update.callback_query.message
            if update.callback_query.message:
                self.chat = update.callback_query.message.chat
            self.user = update.callback_query.user
        elif update.update_type is api.UpdateType.shipping_query:
            self.user = update.shipping_query.user
        elif update.update_type is api.UpdateType.pre_checkout_query:
            self.user = update.pre_checkout_query.user


context = Context.instance()
