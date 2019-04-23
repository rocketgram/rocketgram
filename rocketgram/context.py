# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).


from contextvars import ContextVar
from typing import TYPE_CHECKING, List, Dict

if TYPE_CHECKING:
    from .bot import Bot
    from .update import Update
    from .requests import Request
    from .executors import Executor
    from .connectors import Connector

current_executor = ContextVar('current_executor')
current_bot = ContextVar('current_bot')
current_update = ContextVar('current_update')
current_webhook_requests = ContextVar('current_webhook_requests')


def executor() -> 'Executor':
    v = current_executor.get()
    assert v, "`executor` should not be accessed bot's context."
    return v


def connector() -> 'Connector':
    v = current_bot.get()
    assert v, "`connector()` should not be accessed bot's context."
    return v.connector


def bot() -> 'Bot':
    v = current_bot.get()
    assert v, "`bot()` should not be accessed outside bot's context."
    return v


def globals() -> Dict:
    v = current_bot.get()
    assert v, "`bot()` should not be accessed outside bot's context."
    return v.globals


def update() -> 'Update':
    v = current_update.get()
    assert v, "`update()` should not be accessed outside request's context."
    return v


def webhook_request(request: 'Request'):
    whrs = current_webhook_requests.get()
    whrs.append(request)


def get_webhook_requests() -> List['Request']:
    return current_webhook_requests.get() or list()
