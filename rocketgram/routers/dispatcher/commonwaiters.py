# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from . import commonfilters
from .waiters import make_waiter, DropWaiter
from ...api import UpdateType, MessageType
from ...context import context


@make_waiter
@commonfilters.update_type(UpdateType.message)
def next_message(*message_types: MessageType):
    """\
    Waits next message.

    :param message_types: Wanted `MessageType`. Default `MessageType.text`.

    :return: True or False
    """
    if not message_types:
        message_types = (MessageType.text,)

    if context.message.message_type in message_types:
        return True

    return False


def drop_waiter() -> DropWaiter:
    """\
    Drops current waiter.

    :return: DropWaiter instance
    """

    return DropWaiter()
