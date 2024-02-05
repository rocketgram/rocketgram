# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from contextlib import suppress
from typing import Type

from .base_adapter import BaseJsonAdapter
from .standard_json_adapter import StandardJsonAdapter

with suppress(ImportError):
    from .ujson_adapter import UJsonJsonAdapter

with suppress(ImportError):
    from .orjson_adapter import OrJsonJsonAdapter


def default_json_adapter() -> Type[BaseJsonAdapter]:
    with suppress(NameError):
        return OrJsonJsonAdapter

    with suppress(NameError):
        return UJsonJsonAdapter

    return StandardJsonAdapter
