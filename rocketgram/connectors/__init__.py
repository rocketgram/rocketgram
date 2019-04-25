# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).

from contextlib import suppress

with suppress(ModuleNotFoundError):
    from .aiohttpconnector import AioHttpConnector
with suppress(ModuleNotFoundError):
    from .tornadoconnector import TornadoConnector

from .connector import Connector
