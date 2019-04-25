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

    v = current_executor.get()
    assert v, "`executor` should not be accessed bot's context."
    return v


def bot() -> 'Bot':
    """Returns Bot object for current request."""

    v = current_bot.get()
    assert v, "`bot()` should not be accessed outside bot's context."
    return v


def update() -> 'Update':
    """Returns Update object for current request."""
    v = current_update.get()
    assert v, "`update()` should not be accessed outside request's context."
    return v


def message() -> 'Message':
    """Returns Message object for current request."""

    msg = current_message.get()
    assert msg, "`message()` should not be accessed outside bot's context."
    return msg


def chat() -> 'Chat':
    """Returns Chat object for current request."""

    ch = current_chat.get()
    assert ch, "`chat()` should not be accessed outside bot's context."
    return ch


def user() -> 'User':
    """Returns User object for current request."""

    usr = current_user.get()
    assert usr, "`user()` should not be accessed outside bot's context."
    return usr


def webhook_request(request: 'Request'):
    whrs = current_webhook_requests.get()
    whrs.append(request)


def get_webhook_requests() -> List['Request']:
    return current_webhook_requests.get() or list()
