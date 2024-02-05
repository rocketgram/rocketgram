# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


import ujson

from .base_adapter import BaseJsonAdapter


class UJsonJsonAdapter(BaseJsonAdapter):
    dumps = staticmethod(ujson.dumps)
    loads = staticmethod(ujson.loads)
