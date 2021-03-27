# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


import logging

from ..api import Request, Response
from ..version import version

logger = logging.getLogger('rocketgram.connectors.connector')


class Connector:
    USER_AGENT = f'Rocketgram/{version()}'
    HEADERS = {'Content-Type': 'application/json', 'User-Agent': USER_AGENT}
    API_URL = "https://api.telegram.org/bot%s/"
    API_FILE_URL = "https://api.telegram.org/file/bot%s/%s"

    def __init__(self, *, timeout: int = 35, api_url: str = API_URL, api_file_url: str = API_FILE_URL):
        self._api_file_url = api_file_url
        self._api_url = api_url
        self._timeout = timeout

    async def init(self):
        raise NotImplementedError

    async def shutdown(self):
        raise NotImplementedError

    async def send(self, token: str, request: Request) -> Response:
        raise NotImplementedError

    def resolve_file_url(self, token: str, file_path: str) -> str:
        return self._api_file_url % (token, file_path)
