# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).


from .bot import Bot, Context
from .dispatchers import simpledispatcher
from .exceptions import *
from .executors.updates import UpdatesExecutor
from .executors.webhooks import WebHooksExecutor
from .inlineresults import *
from .keyboards import *


@property
def version():
    return "2019.02"
