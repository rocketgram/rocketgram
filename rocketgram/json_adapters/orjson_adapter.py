# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


import orjson

from .base_adapter import BaseJsonAdapter


class OrJsonJsonAdapter(BaseJsonAdapter):
    dumps = staticmethod(orjson.dumps)
    loads = staticmethod(orjson.loads)
