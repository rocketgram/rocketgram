# Copyright (C) 2015-2024 by Vd.
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

    @property
    def method(self) -> str:
        return self.__class__.__name__

    def render(self, with_method=False) -> dict:
        """Return dict representation of this request object."""

        assert self.__class__.__name__ != 'Request'

        d = asdict(self)

        if with_method:
            d['method'] = self.__class__.__name__

        return self.__prepare(d)

    def files(self) -> List['api.InputFile']:
        """Returns list of binary files that exist in request."""

        return list()

    def parse_result(self, data):
        """Parses the result field of a Response object."""

        raise NotImplementedError

    async def send(self):
        """Sends this request with current context."""

        raise NotImplementedError

    def webhook(self):
        """\
        Schedules sending this request through the webhook-request mechanism.

        For more information see: https://core.telegram.org/bots/api#making-requests-when-getting-updates
        """

        context.webhook(self)
