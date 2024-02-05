# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from contextlib import suppress

from .executor import Executor
from .updates import UpdatesExecutor
from .webhook import WebhookExecutor

with suppress(ImportError):
    from .aiohttp import AioHttpExecutor
