# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).

from contextlib import suppress

with suppress(ImportError):
    from .aiohttp import AioHttpConnector
with suppress(ImportError):
    from .tornado import TornadoConnector

from .connector import Connector
