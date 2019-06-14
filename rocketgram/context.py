# Copyright (C) 2015-2019 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).

import logging
import warnings
from contextvars import ContextVar
from typing import TYPE_CHECKING, List, Optional

if TYPE_CHECKING:
    from .bot import Bot
    from .update import Update, Message, Chat, User
    from .requests import Request
    from .executors import Executor

current_executor = ContextVar('current_executor')
current_bot = ContextVar('current_bot')
current_webhook_requests = ContextVar('current_webhook_requests')

current_update = ContextVar('current_update')
current_message = ContextVar('current_message')
current_chat = ContextVar('current_chat')
current_user = ContextVar('current_user')

logger = logging.getLogger('rocketgram.context')


class Context:
    __slots__ = tuple()

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
    def update(self) -> Optional['Update']:
        """Returns Update object for current request."""

        return current_update.get(None)

    @update.setter
    def update(self, update: 'Update'):
        current_update.set(update)

    @property
    def message(self) -> Optional['Message']:
        """Returns Message object for current request."""

        return current_message.get(None)

    @message.setter
    def message(self, update: 'Message'):
        current_message.set(update)

    @property
    def chat(self) -> Optional['Chat']:
        """Returns Chat object for current request."""

        return current_chat.get(None)

    @chat.setter
    def chat(self, chat: 'Chat'):
        current_chat.set(chat)

    @property
    def user(self) -> Optional['User']:
        """Returns User object for current request."""

        return current_user.get(None)

    @user.setter
    def user(self, user: 'User'):
        current_user.set(user)

    @staticmethod
    def webhook(request: 'Request'):
        """Sets Request object to be sent through webhook-request mechanism."""

        current_webhook_requests.get().append(request)

    @property
    def webhook_requests(self) -> List['Request']:
        """Returns list of current requests awaits sent through webhook-request mechanism."""

        return current_webhook_requests.get()

    @webhook_requests.setter
    def webhook_requests(self, webhook_requests):
        """Returns list of current requests awaits sent through webhook-request mechanism."""

        current_webhook_requests.set(webhook_requests)


context2 = Context()
del Context


def executor() -> Optional['Executor']:
    """Returns Executor object for current request."""

    warnings.warn("Old context-helpers will be removed in 2.0. Use context2 instead.", DeprecationWarning)

    return current_executor.get()


def bot() -> Optional['Bot']:
    """Returns current Bot object."""

    warnings.warn("Old context-helpers will be removed in 2.0. Use context2 instead.", DeprecationWarning)

    return current_bot.get()


def update() -> Optional['Update']:
    """Returns Update object for current request."""

    warnings.warn("Old context-helpers will be removed in 2.0. Use context2 instead.", DeprecationWarning)

    return current_update.get()


def message() -> Optional['Message']:
    """Returns Message object for current request."""

    warnings.warn("Old context-helpers will be removed in 2.0. Use context2 instead.", DeprecationWarning)

    return current_message.get()


def chat() -> Optional['Chat']:
    """Returns Chat object for current request."""

    warnings.warn("Old context-helpers will be removed in 2.0. Use context2 instead.", DeprecationWarning)

    return current_chat.get()


def user() -> Optional['User']:
    """Returns User object for current request."""

    warnings.warn("Old context-helpers will be removed in 2.0. Use context2 instead.", DeprecationWarning)

    return current_user.get()


def webhook_request(request: 'Request'):
    warnings.warn("Old context-helpers will be removed in 2.0. Use context2 instead.", DeprecationWarning)

    current_webhook_requests.get().append(request)


def get_webhook_requests() -> List['Request']:
    warnings.warn("Old context-helpers will be removed in 2.0. Use context2 instead.", DeprecationWarning)

    try:
        return current_webhook_requests.get()
    except LookupError:
        lst = list()
        current_webhook_requests.set(lst)
        return lst
