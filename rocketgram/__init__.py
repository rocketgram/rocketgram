# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).

from .types import *
from .errors import *
from .requests import *
from .update import *
from .inlineresults import *
from .keyboards import *
from .bot import Bot
from .context import Context
from .middlewares import *
from .routers import *
from .executors import *


@property
def version():
    return "2019.03"
