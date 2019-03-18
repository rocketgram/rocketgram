# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).


from .bot import Bot
from .context import Context
from .errors import *
from .executors import *
from .inlineresults import *
from .keyboards import *
from .requests import *
from .routers import *
from .update import *


@property
def version():
    return "2019.03"
