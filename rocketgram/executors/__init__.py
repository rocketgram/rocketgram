# Copyright (C) 2015-2019 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from contextlib import suppress

from .executor import Executor
from .updates import UpdatesExecutor

with suppress(ModuleNotFoundError):
    from .aiohttp import AioHttpExecutor
with suppress(ModuleNotFoundError):
    from .tornado import TornadoExecutor
