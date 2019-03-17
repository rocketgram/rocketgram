# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).


import typing

from .filters import make_filter
from ...update import UpdateType, MessageType

if typing.TYPE_CHECKING:
    from ...context import Context

__all__ = ['command', 'callback', 'update_type', 'message_type', 'chat_type', 'catch_all']


@make_filter
def command(ctx: 'Context', *commands: str, case_sensitive=False, separator=' '):
    """Filters message begins with one of commands.
    Filters commands for other bots in groups.
    Assumes update_type == message and message_type == text.

    :param ctx:
    :param commands:
    :param case_sensitive:
    :param separator:

    :return: True or False
    """

    if ctx.update.update_type != UpdateType.message:
        return False
    if ctx.update.message.message_type != MessageType.text:
        return False

    splitted = ctx.update.message.text.split(sep=separator)
    text = splitted[0]
    if not case_sensitive:
        text = text.lower()

    for cmd in commands:
        if not case_sensitive:
            cmd = cmd.lower()
        if text == cmd or text == cmd + '@' + ctx.bot.name:
            return True

    # args = (command, splitted[1:], separator.join(splitted[1:]))

    return False


@make_filter
def callback(ctx: 'Context', *commands: str, case_sensitive=False, separator=' '):
    """Filters callback query begins with one of commands.
    Assumes update_type == callback_query.

    :param ctx:
    :param commands:
    :param case_sensitive:
    :param separator:
    :return: True or False
    """

    if ctx.update.update_type != UpdateType.callback_query:
        return False

    splited = ctx.update.callback_query.data.split(sep=separator)
    text = splited[0]
    if not case_sensitive:
        text = text.lower()

    for cmd in commands:
        if not case_sensitive:
            cmd = cmd.lower()
        if text == cmd:
            # args = (command, splited[1:], separator.join(splited[1:]))
            return True

    return False


@make_filter
def update_type(ctx: 'Context', *types):
    """Filters updates with selected types.

    :param ctx:
    :param update_types:
    :param message_types:
    :param from_inline:
    :return: True or False
    """

    if ctx.update.update_type in types:
        return True

    return False


@make_filter
def message_type(ctx: 'Context', *types):
    """Filters massage_type with one of selected types.
    Assumes update_type one of message, edited_message, channel_post, edited_channel_post.

    :param ctx:
    :param types:
    :return: True or False
    """

    m = None

    if ctx.update.update_type is UpdateType.message:
        m = ctx.update.message
    elif ctx.update.update_type is UpdateType.edited_message:
        m = ctx.update.edited_message
    elif ctx.update.update_type is UpdateType.channel_post:
        m = ctx.update.channel_post
    elif ctx.update.update_type is UpdateType.edited_channel_post:
        m = ctx.update.edited_channel_post
    else:
        return False

    if m.message_type not in types:
        return False

    return True


@make_filter
def chat_type(ctx: 'Context', *types):
    """Filters chat_type with one of selected types.
    Assumes update_type one of message, edited_message, channel_post, edited_channel_post, callback_query.
    Note: For callbacks it not works for callbacks from messages posted through inline query.

    :param ctx:
    :param types:
    :return: True or False
    """

    m = None

    if ctx.update.update_type is UpdateType.message:
        m = ctx.update.message
    elif ctx.update.update_type is UpdateType.edited_message:
        m = ctx.update.edited_message
    elif ctx.update.update_type is UpdateType.channel_post:
        m = ctx.update.channel_post
    elif ctx.update.update_type is UpdateType.edited_channel_post:
        m = ctx.update.edited_channel_post
    elif ctx.update.update_type is UpdateType.callback_query:
        m = ctx.update.callback_query.message
    else:
        return False

    if not m:
        return False

    if m.chat.chat_type not in types:
        return False

    return True


@make_filter
def catch_all(ctx: 'Context'):
    """\
    Simply catch all updates.

    :return: always True
    """

    return True
