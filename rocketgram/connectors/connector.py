# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).


import logging

from .. import version
from ..requests import Request
from ..update import Response

logger = logging.getLogger('rocketgram.connectors.connector')

USER_AGENT = f'Rocketgram/{version()}'


class Connector:
    async def init(self):
        raise NotImplementedError

    async def shutdown(self):
        raise NotImplementedError

    async def send(self, token: str, request: Request) -> Response:
        raise NotImplementedError
