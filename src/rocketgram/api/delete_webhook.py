# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class DeleteWebhook(BoolResultMixin, Request):
    """\
    Represents DeleteWebhook request object:
    https://core.telegram.org/bots/api#deletewebhook
    """

    drop_pending_updates: Optional[bool] = None
