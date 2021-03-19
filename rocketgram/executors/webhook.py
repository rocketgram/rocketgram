# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


import asyncio
import logging
import signal
from typing import TYPE_CHECKING, Union, Dict, List, Set, Optional

from .executor import Executor
from ..api import Request, GetMe, SetWebhook, DeleteWebhook
from ..api import UpdateType, InputFile
from ..errors import RocketgramRequestError
from ..version import version

try:
    import ujson as json
except ImportError:
    import json

if TYPE_CHECKING:
    from ..bot import Bot

logger = logging.getLogger('rocketgram.executors.webhook')


class WebhookExecutor(Executor):
    HEADERS = {"Server": f"Rocketgram/{version()}", "Content-Type": "application/json"}
    HEADERS_ERROR = {"Server": f"Rocketgram/{version()}", "Content-Type": "text/plain"}

    def __init__(self, base_url: str, base_path: str, *, host: str = 'localhost', port: int = 8080):
        self._base_url = base_url
        self._base_path = base_path
        self._host = host
        self._port = port

        self._bots = dict()
        self._srv = None
        self._started = False

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
                      max_connections: int = None):

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

        await bot.init()

        self._bots[full_path] = bot
        logger.info('Added bot @%s', bot.name)

        if set_webhook or drop_pending_updates:
            swh = SetWebhook(full_url, certificate=certificate, ip_address=ip_address, allowed_updates=allowed_updates,
                             drop_pending_updates=drop_pending_updates, max_connections=max_connections)
            await bot.send(swh)
            logger.debug('Webhook setup done for bot @%s', bot.name)

        if drop_pending_updates:
            logger.debug('Updates dropped for @%s', bot.name)

    async def remove_bot(self, bot: 'Bot', delete_webhook: bool = True):
        if bot not in self._bots.values():
            raise ValueError('Bot was not found.')

        self._bots = {k: v for k, v in self._bots.items() if v != bot}

        if bot in self._tasks:
            tasks = self._tasks[bot]
            self._tasks[bot] = set()
            await self._wait_tasks(tasks)

        if delete_webhook:
            try:
                await bot.send(DeleteWebhook())
            except RocketgramRequestError:
                logger.error('Error while removing webhook for %s.' % bot.name)

        await bot.shutdown()

        logger.info('Removed bot @%s', bot.name)

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
            signals: tuple = (signal.SIGINT, signal.SIGTERM), shutdown_wait: int = 10):

        executor = cls(base_url, base_path, host=host, port=port)

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
