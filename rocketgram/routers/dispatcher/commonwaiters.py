# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).


import typing

from . import commonfilters
from .filters import make_waiter
from ...update import UpdateType, MessageType

if typing.TYPE_CHECKING:
    from ...context import Context


@make_waiter
@commonfilters.update_type(UpdateType.message)
def next_message(ctx: 'Context', *message_types: MessageType):
    """\
    Waits next message.

    :param ctx: `Context`.
    :param message_types: Wanted `MessageType`. Default `MessageType.text`.
    :return:
    """
    if not message_types:
        message_types = (MessageType.text,)

    if ctx.update.message.message_type in message_types:
        return True

    return False
