# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from typing import Union, Any


class BaseJsonAdapter:
    @staticmethod
    def dumps(obj: Any, **kwargs) -> str:
        raise NotImplementedError

    @staticmethod
    def loads(s: Union[str, bytes, bytearray], **kwargs) -> Any:
        raise NotImplementedError
