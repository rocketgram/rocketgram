# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).


import typing

from .base import FilterResult
from ...update import UpdateType, MessageType, ChatType

if typing.TYPE_CHECKING:
    from ...context import Context


def cmd(command: str, chat_types=(ChatType.private,), *, case_sensitive=False, separator=' '):
    """Filters message begins with selected command.
    Filters commands for other bots in groups.

    :param command:
    :param chat_types:
    :param case_sensitive:
    :param separator:

    :return: False or FilterResult((command, splitted, joined))

    """

    def cmd_filter(ctx: 'Context'):
        if ctx.update.update_type != UpdateType.message:
            return False
        if ctx.update.message.message_type != MessageType.text:
            return False

        if ctx.update.message.chat._type not in chat_types:
            return False

        splitted = ctx.update.message.text.split(sep=separator)
        text = splitted[0]
        c = command
        if not case_sensitive:
            text = text.lower()
            c = c.lower()

        if not (text == c or text == c + '@' + ctx.bot.name):
            return False

        args = (command, splitted[1:], separator.join(splitted[1:]))

        return FilterResult(args)

    return cmd_filter


def cb(command: str, *, message=True, inline=False, case_sensitive=False, separator=' '):
    """Filters callback query begins with selected command.
    Filters commands for other bots in groups.

    :param command:
    :param message:
    :param inline:
    :param case_sensitive:
    :param separator:
    :return: False or FilterResult((command, splitted, joined))

    """

    def cb_filter(ctx):
        if ctx.update.update_type != UpdateType.callback_query:
            return False
        if not message and ctx.update.callback_query.message is not None:
            return False
        if not inline and ctx.update.callback_query.inline_message_id is not None:
            return False

        splited = ctx.update.message.text.split(sep=separator)
        text = splited[0]
        cmd = command
        if not case_sensitive:
            text = text.lower()
            cmd = cmd.lower()

        if not (text == cmd or text == cmd + '@' + ctx.bot.name):
            return False

        args = (command, splited[1:], separator.join(splited[1:]))

        return FilterResult(args)

    return cb_filter


def types(*, update_types=UpdateType.message, message_types=MessageType.text, from_inline=False):
    """Filters updates with selected types.

    :param update_types:
    :param message_types:
    :param from_inline:
    :return: False or FilterResult(None)
    """

    if not isinstance(update_types, (tuple, list)):
        update_types = (update_types,)

    if not isinstance(message_types, (tuple, list)):
        message_types = (message_types,)

    def types_filter(ctx: 'Context'):

        if ctx.update.update_type not in update_types:
            return False

        m = None

        if ctx.update.update_type is UpdateType.message:
            m = ctx.update.message
        elif ctx.update.update_type is UpdateType.edited_message:
            m = ctx.update.edited_message
        elif ctx.update.update_type is UpdateType.channel_post:
            m = ctx.update.channel_post
        elif ctx.update.update_type is UpdateType.edited_channel_post:
            m = ctx.update.edited_channel_post

        if m is not None:
            if m.message_type not in message_types:
                return False

        if ctx.update.update_type is UpdateType.callback_query:
            if ctx.update.callback_query.inline_message_id is not None:
                if not from_inline:
                    return False
            else:
                if ctx.update.callback_query.message is None:
                    return False
                if ctx.update.callback_query.message.message_type not in message_types:
                    return False

        return FilterResult(None)

    return types_filter
