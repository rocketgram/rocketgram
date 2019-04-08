# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).

import typing

from . import commonfilters
from .filters import make_waiter
from ...update import MessageType

if typing.TYPE_CHECKING:
    from ...context import Context


@make_waiter
@commonfilters.message_type(MessageType.text)
def next_message(ctx: 'Context'):
    """Waits new text message."""
    return True
