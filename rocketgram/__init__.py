# Copyright (C) 2015-2019 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).

from contextlib import suppress

with suppress(ModuleNotFoundError):
    import uvloop

    uvloop.install()

from . import context
from . import tools
from .bot import Bot
from .connectors import *
from .errors import *
from .executors import *
from .keyboards import *
from .middlewares import *
from .requests import *
from .routers import *
from .types import *
from .update import *
from .version import version
