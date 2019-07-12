# Copyright (C) 2015-2019 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).

from contextlib import suppress

from .defaultvalues import DefaultValuesMiddleware
from .limiter import LimiterMiddleware
from .middleware import Middleware, EmptyMiddleware

with suppress(ImportError):
    from .prometheus import PrometheusMiddleware
