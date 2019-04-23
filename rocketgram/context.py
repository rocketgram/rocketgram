# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).


import logging
from contextvars import ContextVar
from typing import TYPE_CHECKING, List, Dict

from .update import Update
from .update import UpdateType

if TYPE_CHECKING:
    from .bot import Bot
    from .requests import Request
    from .executors import Executor
    from .connectors import Connector

logger = logging.getLogger('rocketgram.context')

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


class ContextRequests:
    @staticmethod
    def send_message(text, parse_mode=None, disable_web_page_preview=None, disable_notification=None,
                     reply_to_message_id=None, reply_markup=None):
        """https://core.telegram.org/bots/api#sendmessage"""

        if update().update_type is UpdateType.message:
            chat_id = update().message.chat.chat_id
        elif update().update_type is UpdateType.edited_message:
            chat_id = update().edited_message.chat.chat_id
        elif update().update_type is UpdateType.channel_post:
            chat_id = update().channel_post.chat.chat_id
        elif update().update_type is UpdateType.edited_channel_post:
            chat_id = update().edited_channel_post.chat.chat_id
        elif update().update_type is UpdateType.callback_query and update().callback_query.message:
            chat_id = update().callback_query.message.chat.chat_id
        elif update().update_type is UpdateType.shipping_query:
            chat_id = update().shipping_query.user.user_id
        elif update().update_type is UpdateType.pre_checkout_query:
            chat_id = update().pre_checkout_query.user.user_id
        else:
            raise TypeError('Wrong update type')

        return bot().send_message(chat_id, text, parse_mode=parse_mode,
                                  disable_web_page_preview=disable_web_page_preview,
                                  disable_notification=disable_notification,
                                  reply_to_message_id=reply_to_message_id, reply_markup=reply_markup)

    @staticmethod
    def reply_message(text, parse_mode=None, disable_web_page_preview=None, disable_notification=None,
                      reply_markup=None):
        """https://core.telegram.org/bots/api#sendmessage"""

        if update().update_type is UpdateType.message:
            chat_id = update().message.chat.chat_id
            reply_to_message_id = update().message.message_id
        elif update().update_type is UpdateType.edited_message:
            chat_id = update().edited_message.chat.chat_id
            reply_to_message_id = update().edited_message.message_id
        elif update().update_type is UpdateType.channel_post:
            chat_id = update().channel_post.chat.chat_id
            reply_to_message_id = update().channel_post.message_id
        elif update().update_type is UpdateType.edited_channel_post:
            chat_id = update().edited_channel_post.chat.chat_id
            reply_to_message_id = update().edited_channel_post.message_id
        elif update().update_type is UpdateType.callback_query and update().callback_query.message:
            chat_id = update().callback_query.message.chat.chat_id
            reply_to_message_id = update().callback_query.message.message_id
        else:
            raise TypeError('Wrong update type')

        return bot().send_message(chat_id, text, parse_mode=parse_mode,
                                  disable_web_page_preview=disable_web_page_preview,
                                  disable_notification=disable_notification,
                                  reply_to_message_id=reply_to_message_id, reply_markup=reply_markup)

    @staticmethod
    def answer_callback_query(text=None, show_alert=None, url=None, cache_time=None):
        """https://core.telegram.org/bots/api#answercallbackquery"""

        if not update().update_type is UpdateType.callback_query:
            raise TypeError('Wrong update type')

        return bot().answer_callback_query(update().callback_query.query_id, text=text, show_alert=show_alert,
                                           url=url,
                                           cache_time=cache_time)

    @staticmethod
    def send_or_answer(text, parse_mode=None, disable_web_page_preview=None, disable_notification=None,
                       reply_to_message_id=None, reply_markup=None, show_alert=None, url=None, cache_time=None):
        """https://core.telegram.org/bots/api#sendmessage
        https://core.telegram.org/bots/api#answercallbackquery"""

        if update().update_type is UpdateType.callback_query and update().callback_query.message:
            return bot().answer_callback_query(update().callback_query.query_id, text=text,
                                               show_alert=show_alert, url=url,
                                               cache_time=cache_time)

        if update().update_type is UpdateType.message:
            chat_id = update().message.chat.chat_id
        elif update().update_type is UpdateType.edited_message:
            chat_id = update().edited_message.chat.chat_id
        elif update().update_type is UpdateType.channel_post:
            chat_id = update().channel_post.chat.chat_id
        elif update().update_type is UpdateType.edited_channel_post:
            chat_id = update().edited_channel_post.chat.chat_id
        elif update().update_type is UpdateType.shipping_query:
            chat_id = update().shipping_query.user.user_id
        elif update().update_type is UpdateType.pre_checkout_query:
            chat_id = update().pre_checkout_query.user.user_id
        else:
            raise TypeError('Wrong update type')

        return bot().send_message(chat_id, text, parse_mode=parse_mode,
                                  disable_web_page_preview=disable_web_page_preview,
                                  disable_notification=disable_notification,
                                  reply_to_message_id=reply_to_message_id, reply_markup=reply_markup)

    @staticmethod
    def send_or_edit(text, parse_mode=None, disable_web_page_preview=None, disable_notification=None,
                     reply_to_message_id=None, reply_markup=None):
        """https://core.telegram.org/bots/api#sendmessage
        https://core.telegram.org/bots/api#editmessagetext"""

        if update().update_type == UpdateType.message:
            return bot().send_message(update().message.chat.chat_id, text, parse_mode=parse_mode,
                                      disable_web_page_preview=disable_web_page_preview,
                                      disable_notification=disable_notification,
                                      reply_to_message_id=reply_to_message_id, reply_markup=reply_markup)
        else:
            return bot().edit_message_text(chat_id=update().callback_query.message.chat.chat_id,
                                           message_id=update().callback_query.message.message_id, text=text,
                                           parse_mode=parse_mode,
                                           disable_web_page_preview=disable_web_page_preview,
                                           reply_markup=reply_markup)

    @staticmethod
    def edit_message_text(text, parse_mode=None, disable_web_page_preview=None, reply_markup=None):
        """https://core.telegram.org/bots/api#editmessagetext"""

        if not update().update_type is UpdateType.callback_query:
            raise TypeError('Wrong update type')

        if update().callback_query.message:
            return bot().edit_message_text(chat_id=update().callback_query.message.chat.chat_id,
                                           message_id=update().callback_query.message.message_id, text=text,
                                           parse_mode=parse_mode,
                                           disable_web_page_preview=disable_web_page_preview,
                                           reply_markup=reply_markup)
        else:
            return bot().edit_message_text(inline_message_id=update().callback_query.inline_message_id,
                                           text=text,
                                           parse_mode=parse_mode,
                                           disable_web_page_preview=disable_web_page_preview,
                                           reply_markup=reply_markup)
