# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass, asdict
from datetime import datetime
from enum import Enum
from typing import Union, Dict, List

from .. import api
from ..context import context
from ..keyboards import keyboard


@dataclass(frozen=True)
class Request:
    """\
    Base class for all request objects.
    """

    method = None

    def __prepare(self, d: Union[Dict, List]) -> Union[Dict, List]:
        assert isinstance(d, (list, dict))

        for k, v in d.items() if isinstance(d, dict) else enumerate(d):
            if isinstance(v, Enum):
                d[k] = v.value
                continue
            if isinstance(v, datetime):
                d[k] = int(v.timestamp())
                continue
            if isinstance(v, api.InputFile):
                d[k] = f'attach://{v.file_name}'
                continue
            if isinstance(v, keyboard.Keyboard):
                d[k] = self.__prepare(asdict(v.render()))
                continue
            if isinstance(v, (list, dict)):
                d[k] = self.__prepare(v)

        if isinstance(d, dict):
            return {k: v for k, v in d.items() if v is not None}
        return [v for v in d if v is not None]

    def render(self, with_method=False) -> dict:
        assert self.method

        d = asdict(self)

        assert 'method' not in d

        if with_method:
            d['method'] = self.method

        return self.__prepare(d)

    def files(self) -> List['api.InputFile']:
        return list()

    async def send(self) -> 'api.Response':
        return await context.bot.send(self)

    def webhook(self):
        context.webhook(self)
