# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from .filters import make_filter
from ...api import UpdateType, MessageType, ChatType
from ...context import context


@make_filter
def command(*commands: str, case_sensitive: bool = False, separator: str = ' '):
    """Filters messages begin with one of the commands.
    Filters commands for other bots in groups.
    Assumes update_type == message and message_type == text.

    :param commands:
    :param case_sensitive:
    :param separator:

    :return: True or False
    """

    if context.update.type is not UpdateType.message:
        return False

    msg = context.message
    if not msg:
        return False
    if msg.type is not MessageType.text:
        return False

    split = msg.text.split(sep=separator)
    text = split[0] if case_sensitive else split[0].lower()
    bot_name = context.bot.name if case_sensitive else context.bot.name.lower()

    for cmd in commands:
        if not case_sensitive:
            cmd = cmd.lower()
        if text == cmd or text == cmd + '@' + bot_name:
            return True

    return False


@make_filter
def deeplink(*commands: str, case_sensitive: bool = False):
    """Filters deep links parameters passed to /start command.
    If no commands were present, then all deep links will be cached.
    Filters commands for other bots in groups.
    Assumes update_type == message and message_type == text.

    :param commands:
    :param case_sensitive:

    :return: True or False
    """

    if context.update.type is not UpdateType.message:
        return False

    msg = context.message
    if not msg:
        return False
    if msg.type is not MessageType.text:
        return False

    text = msg.text
    text_lw = msg.text.lower()
    lw = '/start@%s ' % context.bot.name.lower()

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
    """Filters a callback query begin with one of the commands.
    Assumes update_type == callback_query.

    :param commands:
    :param case_sensitive:
    :param separator:

    :return: True or False
    """

    if context.update.type is not UpdateType.callback_query:
        return False

    if context.update.callback_query.data is None:
        return False

    split = context.update.callback_query.data.split(sep=separator)
    text = split[0]
    if not case_sensitive:
        text = text.lower()

    for cmd in commands:
        if not case_sensitive:
            cmd = cmd.lower()
        if text == cmd:
            return True

    return False


@make_filter
def game(*names: str, case_sensitive: bool = False):
    """Filters callback query if it is a game with one of certain names.
    Assumes update_type == callback_query.

    :param names:
    :param case_sensitive:

    :return: True or False
    """

    if context.update.type is not UpdateType.callback_query:
        return False

    if context.update.callback_query.game_short_name is None:
        return False

    text = context.update.callback_query.game_short_name.strip()
    if not case_sensitive:
        text = text.lower()

    for name in names:
        if not case_sensitive:
            name = name.lower()
        if text == name:
            return True

    return False


@make_filter
def inline_callback():
    """Filters callback_query done in messages posted through inline query.
    Assumes update_type is callback_query.

    :return: True or False
    """

    if context.update.type is not UpdateType.callback_query:
        return False

    if context.update.callback_query.inline_message_id is None:
        return False

    return True


@make_filter
def inline(*commands: str, case_sensitive: bool = False):
    """Filters inline_query begin with one of the commands.
    Assumes update_type is inline_query.

    :param commands:
    :param case_sensitive:
    :return: True or False
    """

    if context.update.type is not UpdateType.inline_query:
        return False

    text = context.update.inline_query.query

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
    """Filters chosen_inline_result with a query begins with one of the commands.
    Assumes update_type is chosen_inline_result.

    :param commands:
    :param case_sensitive:

    :return: True or False
    """

    if context.update.type is not UpdateType.chosen_inline_result:
        return False

    text = context.update.chosen_inline_result.query

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

    :param types:

    :return: True or False
    """

    return context.update.type in types


@make_filter
def message_type(*types: MessageType):
    """Filters massage_type with one of selected types.
    Assumes update_type one of message, edited_message, channel_post, edited_channel_post.

    :param types:
    :return: True or False
    """

    msg = context.message

    if not msg:
        return False

    return msg.type in types


@make_filter
def chat_type(*types: ChatType):
    """Filters chat_type with one of the selected types.
    Assumes update_type one of messages, edited_message, channel_post, edited_channel_post, callback_query.
    Note: It does not work for callbacks from messages posted through an inline query.

    :param types:
    
    :return: True or False
    """

    ch = context.chat

    if not ch:
        return False

    return ch.type in types


@make_filter
def catch_all():
    """\
    Catches all updates.

    :return: always True
    """

    return True
