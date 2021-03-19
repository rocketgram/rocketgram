# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, Any

from .. import api


@dataclass(frozen=True)
class Response:
    """\
    Represents Response object:
    https://core.telegram.org/bots/api#making-requests

    Additional fields:
    request
    raw
    """

    request: 'api.Request'
    raw: dict
    ok: bool
    error_code: Optional[int]
    description: Optional[str]
    result: Any
    parameters: Optional['api.ResponseParameters']

    @classmethod
    def parse(cls, data: dict, request: 'api.Request') -> Optional['Response']:
        if data is None:
            return None

        ok = data['ok']
        error_code = data.get('error_code')
        description = data.get('description')
        parameters = api.ResponseParameters.parse(data.get('parameters'))

        if error_code is not None:
            return cls(request, data, ok, error_code, description, None, parameters)

        result = request.parse_result(data['result'])

        return cls(request, data, ok, error_code, description, result, parameters)
