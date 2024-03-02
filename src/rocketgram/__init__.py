# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from .api import *
from .bot import Bot
from .connectors import *
from .context import context
from .errors import *
from .executors import *
from .json_adapters import *
from .keyboards import *
from .middlewares import *
from .routers import *
from . import tools
from .version import version

API_URL = Connector.API_URL
API_FILE_URL = Connector.API_FILE_URL

VERSION = version()
__version__ = VERSION
