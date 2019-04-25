# Copyright (C) 2015-2019 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from contextvars import ContextVar
from typing import TYPE_CHECKING, List

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


def executor() -> 'Executor':
    """Returns Executor object for current request."""

    return current_executor.get()


def bot() -> 'Bot':
    """Returns current Bot object."""

    return current_bot.get()


def update() -> 'Update':
    """Returns Update object for current request."""
    return current_update.get()


def message() -> 'Message':
    """Returns Message object for current request."""

    return current_message.get()


def chat() -> 'Chat':
    """Returns Chat object for current request."""

    return current_chat.get()


def user() -> 'User':
    """Returns User object for current request."""

    return current_user.get()


def webhook_request(request: 'Request'):
    current_webhook_requests.get().append(request)


def get_webhook_requests() -> List['Request']:
    try:
        return current_webhook_requests.get()
    except LookupError:
        lst = list()
        current_webhook_requests.set(lst)
        return lst
