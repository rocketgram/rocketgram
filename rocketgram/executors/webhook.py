# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


import asyncio
import logging
import signal
from secrets import token_urlsafe
from typing import TYPE_CHECKING, Union, Dict, List, Set, Optional, Type, Tuple

from .executor import Executor
from ..api import Request, GetMe, SetWebhook, DeleteWebhook
from ..api import UpdateType, InputFile
from ..errors import RocketgramRequestError
from ..json_adapters import BaseJsonAdapter, default_json_adapter
from ..version import version

if TYPE_CHECKING:
    from ..bot import Bot

logger = logging.getLogger('rocketgram.executors.webhook')


class WebhookExecutor(Executor):
    HEADERS = {"Server": f"Rocketgram/{version()}", "Content-Type": "application/json"}
    HEADERS_ERROR = {"Server": f"Rocketgram/{version()}", "Content-Type": "text/plain"}
    HEADER_SECRET = "X-Telegram-Bot-Api-Secret-Token"

    __slots__ = ('_base_url', '_base_path', '_host', '_port', '_bots', '_srv',
                 '_started', '_tasks', '_dumps', '_loads', '_secret_token', '_secret_tokens')

    def __init__(self, base_url: str, base_path: str, *, host: str = 'localhost', port: int = 8080,
                 secret_token: Union[bool, str] = False,
                 json_adapter: Type[BaseJsonAdapter] = default_json_adapter()):

        self._base_url = base_url
        self._base_path = base_path
        self._host = host
        self._port = port

        self._secret_token = secret_token

        self._bots: Dict[str, 'Bot'] = dict()
        self._secret_tokens: Dict['Bot', Optional[str]] = dict()

        self._srv = None
        self._started = False

        self._loads = json_adapter.loads
        self._dumps = json_adapter.dumps

        self._tasks: Dict['Bot', Set[asyncio.Task]] = dict()

    @property
    def bots(self) -> List['Bot']:
        return list(self._bots.values())

    @property
    def running(self) -> bool:
        return self._started

    def can_process_webhook_request(self, request: Request) -> bool:
        return len(request.files()) == 0

    async def add_bot(self, bot: 'Bot', *, allowed_updates: Optional[List[UpdateType]] = None,
                      drop_pending_updates: bool = False, certificate: Optional[InputFile] = None,
                      ip_address: Optional[str] = None, suffix: str = None, set_webhook: bool = True,
                      secret_token: Optional[Union[bool, str]] = None, max_connections: int = None):

        if bot in self._bots.values():
            raise ValueError('Bot already added.')

        if not suffix:
            suffix = bot.token

        full_path = self._base_path + suffix
        full_url = self._base_url + suffix

        if bot.name is None:
            response = await bot.send(GetMe())
            bot.name = response.result.username
            logger.info('Bot authorized as @%s', response.result.username)

        await bot.init(self)

        set_secret_token, secret_token = self._gen_secret_token(secret_token)

        self._bots[full_path] = bot
        self._secret_tokens[bot] = secret_token
        self._tasks[bot] = set()

        logger.info('Added bot @%s', bot.name)

        if set_webhook or drop_pending_updates or set_secret_token:
            swh = SetWebhook(full_url, certificate=certificate, ip_address=ip_address, allowed_updates=allowed_updates,
                             drop_pending_updates=drop_pending_updates, secret_token=secret_token,
                             max_connections=max_connections)
            await bot.send(swh)
            logger.debug('Webhook setup done for bot @%s', bot.name)

        if drop_pending_updates:
            logger.debug('Updates dropped for @%s', bot.name)

    async def remove_bot(self, bot: 'Bot', delete_webhook: bool = True):
        if bot not in self._bots.values():
            raise ValueError('Bot was not found.')

        self._bots = {k: v for k, v in self._bots.items() if v != bot}
        del self._secret_tokens[bot]

        if bot in self._tasks:
            tasks = self._tasks[bot]
            del self._tasks[bot]
            await self._wait_tasks(tasks)

        if delete_webhook:
            try:
                await bot.send(DeleteWebhook())
            except RocketgramRequestError:
                logger.error('Error while removing webhook for %s.' % bot.name)

        await bot.shutdown(self)

        logger.info('Removed bot @%s', bot.name)

    def _gen_secret_token(self, secret_token: Optional[Union[bool, str]]) -> Tuple[bool, Optional[str]]:
        secret_token = secret_token if secret_token is not None else self._secret_token

        if not secret_token:
            return False, None

        return (True, token_urlsafe()) if secret_token is True else (False, secret_token)

    async def start(self):
        raise NotImplementedError

    async def stop(self):
        raise NotImplementedError

    @staticmethod
    async def _wait_tasks(tasks: Set[asyncio.Task]):
        while len(tasks):
            logger.info("Waiting %s tasks...", len(tasks))
            _, tasks = await asyncio.wait(tasks, timeout=1, return_when=asyncio.FIRST_COMPLETED)

    @classmethod
    def run(cls, bots: Union['Bot', List['Bot']], base_url: str, base_path: str, *, host: str = 'localhost',
            port: int = 8080, webhook_setup: bool = True, webhook_remove: bool = True,
            certificate: Optional[InputFile] = None, ip_address: Optional[str] = None,
            allowed_updates: Optional[List[UpdateType]] = None, drop_pending_updates: bool = False,
            signals: tuple = (signal.SIGINT, signal.SIGTERM), shutdown_wait: int = 10,
            secret_token: Union[bool, str] = False, json_adapter: Type[BaseJsonAdapter] = default_json_adapter()):

        executor = cls(base_url, base_path, host=host, port=port, secret_token=secret_token, json_adapter=json_adapter)

        def add(bot: 'Bot'):
            return executor.add_bot(bot, certificate=certificate, ip_address=ip_address,
                                    allowed_updates=allowed_updates, drop_pending_updates=drop_pending_updates,
                                    set_webhook=webhook_setup)

        def remove(bot: 'Bot'):
            return executor.remove_bot(bot, delete_webhook=webhook_remove)

        logger.info('Starting webhook executor...')
        logger.debug('Using base url: %s', base_url)
        logger.debug('Using base path: %s', base_path)

        cls._run(executor, add, remove, bots, signals, shutdown_wait=shutdown_wait)
