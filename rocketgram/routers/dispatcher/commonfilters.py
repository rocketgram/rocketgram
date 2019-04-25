# Copyright (C) 2015-2019 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from .filters import make_filter
from ... import context
from ...update import UpdateType, MessageType, ChatType


@make_filter
def command(*commands: str, case_sensitive: bool = False, separator: str = ' '):
    """Filters message begins with one of commands.
    Filters commands for other bots in groups.
    Assumes update_type == message and message_type == text.

    :param commands:
    :param case_sensitive:
    :param separator:

    :return: True or False
    """

    msg = context.message()
    if not msg:
        return False
    if msg.message_type is not MessageType.text:
        return False

    splitted = msg.text.split(sep=separator)
    text = splitted[0] if case_sensitive else splitted[0].lower()
    botname = context.bot().name if case_sensitive else context.bot().name.lower()

    for cmd in commands:
        if not case_sensitive:
            cmd = cmd.lower()
        if text == cmd or text == cmd + '@' + botname:
            return True

    return False


@make_filter
def deeplink(*commands: str, case_sensitive: bool = False):
    """Filters deeplinks parameters passed to /start command.
    If no commands was present then all deeplinks will be cached.
    Filters commands for other bots in groups.
    Assumes update_type == message and message_type == text.

    :param commands:
    :param case_sensitive:
    :param separator:

    :return: True or False
    """

    msg = context.message()
    if not msg:
        return False
    if msg.message_type is not MessageType.text:
        return False

    text = msg.text
    text_lw = msg.text.lower()
    lw = '/start@%s ' % context.bot().name.lower()

    if not (text.startswith('/start ') or text_lw.startswith(lw)):
        return False

    if not len(commands):
        return True

    if not case_sensitive:
        text = text_lw

    if text.lower().startswith(lw):
        text = msg.text[7 + len(lw):]
    else:
        text = msg.text[7:]

    for cmd in commands:
        if not case_sensitive:
            cmd = cmd.lower()
        if text.startswith(cmd):
            return True

    return False


@make_filter
def callback(*commands: str, case_sensitive: bool = False, separator=' '):
    """Filters callback query begins with one of commands.
    Assumes update_type == callback_query.

    :param commands:
    :param case_sensitive:
    :param separator:

    :return: True or False
    """

    if context.update().update_type is not UpdateType.callback_query:
        return False

    splited = context.update().callback_query.data.split(sep=separator)
    text = splited[0]
    if not case_sensitive:
        text = text.lower()

    for cmd in commands:
        if not case_sensitive:
            cmd = cmd.lower()
        if text == cmd:
            return True

    return False


@make_filter
def inline_callback():
    """Filters callback_query done in messages posted through inline query.
    Assumes update_type is callback_query.

    :param types:

    :return: True or False
    """

    if context.update().update_type is not UpdateType.callback_query:
        return False

    if context.update().callback_query.inline_message_id is None:
        return False

    return True


@make_filter
def inline(*commands: str, case_sensitive: bool = False):
    """Filters inline_query begins with one of commands.
    Assumes update_type is inline_query.

    :param commands:
    :param case_sensitive:
    :return: True or False
    """

    if context.update().update_type is not UpdateType.inline_query:
        return False

    text = context.update().inline_query.query

    if not case_sensitive:
        text = text.lower()

    for cmd in commands:
        if not case_sensitive:
            cmd = cmd.lower()
        if text.startswith(cmd):
            return True

    return False


@make_filter
def chosen(*commands: str, case_sensitive: bool = False):
    """Filters chosen_inline_result with query begins with one of commands.
    Assumes update_type is chosen_inline_result.

    :param commands:
    :param case_sensitive:

    :return: True or False
    """

    if context.update().update_type is not UpdateType.chosen_inline_result:
        return False

    text = context.update().chosen_inline_result.query

    if not case_sensitive:
        text = text.lower()

    for cmd in commands:
        if not case_sensitive:
            cmd = cmd.lower()
        if text.startswith(cmd):
            return True

    return False


@make_filter
def update_type(*types: UpdateType):
    """Filters updates with selected types.

    :param update_types:
    :param message_types:
    :param from_inline:

    :return: True or False
    """

    return context.update().update_type in types


@make_filter
def message_type(*types: UpdateType):
    """Filters massage_type with one of selected types.
    Assumes update_type one of message, edited_message, channel_post, edited_channel_post.

    :param types:
    :return: True or False
    """

    msg = context.message()

    if not msg:
        return False

    return context.message().message_type in types


@make_filter
def chat_type(*types: ChatType):
    """Filters chat_type with one of selected types.
    Assumes update_type one of message, edited_message, channel_post, edited_channel_post, callback_query.
    Note: For callbacks it not works for callbacks from messages posted through inline query.

    :param types:
    
    :return: True or False
    """

    ch = context.chat()

    if not ch:
        return False

    return ch.chat_type in types


@make_filter
def catch_all():
    """\
    Simply catch all updates.

    :return: always True
    """

    return True
