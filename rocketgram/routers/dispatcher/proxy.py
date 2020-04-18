# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


import warnings

from .base import BaseDispatcher


class BaseDispatcherProxy(BaseDispatcher):
    def __init__(self, *args, **kwargs):
        warnings.warn("This class is deprecated. Use BaseDispatcher instead.", DeprecationWarning)

        super().__init__(*args, **kwargs)
