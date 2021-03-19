# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


import asyncio
import logging
import signal
from typing import TYPE_CHECKING, Union, Dict, List, Set, Optional

from aiohttp.web import Server, ServerRunner, BaseRequest, TCPSite, Response

from .executor import Executor
from ..api import Request, GetMe, SetWebhook, DeleteWebhook
from ..api import Update, UpdateType
from ..errors import RocketgramRequestError
from ..version import version

try:
    import ujson as json
except ImportError:
    import json

if TYPE_CHECKING:
    from ..bot import Bot

logger = logging.getLogger('rocketgram.executors.aiohttp')

HEADERS = {"Server": f"Rocketgram/{version()}", "Content-Type": "application/json"}
HEADERS_ERROR = {"Server": f"Rocketgram/{version()}", "Content-Type": "text/plain"}


class AioHttpExecutor(Executor):
    def __init__(self, base_url: str, base_path: str, *, host: str = 'localhost', port: int = 8080):
        """

        :param base_url:
        :param base_path:
        :param host:
        :param port:
        """

        self.__base_url = base_url
        self.__base_path = base_path
        self.__host = host
        self.__port = port

        self.__bots = dict()
        self.__srv = None
        self.__started = False

        self.__tasks: Dict['Bot', Set[asyncio.Task]] = dict()

    @property
    def bots(self):
        """

        :return:
        """
        return self.__bots.values()

    @property
    def running(self):
        """

        :rtype: object
        """
        return self.__started

    def can_process_webhook_request(self, request: Request) -> bool:
        return len(request.files()) == 0

    async def add_bot(self, bot: 'Bot', *, allowed_updates: Optional[List[UpdateType]] = None,
                      drop_pending_updates: bool = False, suffix: str = None, set_webhook: bool = True,
                      max_connections: int = None):
        """

        :param bot:
        :param allowed_updates:
        :param drop_pending_updates:
        :param suffix:
        :param set_webhook:
        :param max_connections:
        """
        if bot in self.__bots.values():
            raise ValueError('Bot already added.')

        if not suffix:
            suffix = bot.token

        full_path = self.__base_path + suffix
        full_url = self.__base_url + suffix

        if bot.name is None:
            response = await bot.send(GetMe())
            bot.name = response.result.username
            logger.info('Bot authorized as @%s', response.result.username)

        await bot.init()

        self.__bots[full_path] = bot
        logger.info('Added bot @%s', bot.name)

        if set_webhook or drop_pending_updates:
            swh = SetWebhook(full_url, allowed_updates=allowed_updates, drop_pending_updates=drop_pending_updates,
                             max_connections=max_connections)
            await bot.send(swh)
            logger.debug('Webhook setup done for bot @%s', bot.name)

        if drop_pending_updates:
            logger.debug('Updates dropped for @%s', bot.name)

    async def remove_bot(self, bot: 'Bot', delete_webhook: bool = True):
        """

        :param bot:
        :param delete_webhook:
        """
        if bot not in self.__bots.values():
            raise ValueError('Bot was not found.')

        self.__bots = {k: v for k, v in self.__bots.items() if v != bot}

        if bot in self.__tasks:
            tasks = self.__tasks[bot]
            self.__tasks[bot] = set()
            await self.__wait_tasks(tasks)

        if delete_webhook:
            try:
                await bot.send(DeleteWebhook())
            except RocketgramRequestError:
                logger.error('Error while removing webhook for %s.' % bot.name)

        await bot.shutdown()

        logger.info('Removed bot @%s', bot.name)

    async def __handler(self, request: BaseRequest):
        if request.method != 'POST':
            return Response(status=400, text="Bad request.", headers=HEADERS_ERROR)

        bot = self.__bots.get(request.path)

        if not bot:
            logger.warning("Bot not found for request `%s`.", request.path)
            return Response(status=404, text="Not found.", headers=HEADERS_ERROR)

        if bot not in self.__tasks:
            self.__tasks[bot] = set()

        try:
            parsed = Update.parse(json.loads(await request.read()))
        except Exception:  # noqa
            logger.exception("Got exception while parsing update:")
            return Response(status=500, text="Server error.", headers=HEADERS_ERROR)

        task = asyncio.create_task(
            bot.process(self, parsed))
        self.__tasks[bot].add(task)

        try:
            response: Request = await task
        except Exception:  # noqa
            logger.exception("Got exception while processing update:")
            return Response(status=500, text="Server error.", headers=HEADERS_ERROR)

        if response:
            data = json.dumps(response.render(with_method=True))
            return Response(body=data, headers=HEADERS)

        self.__tasks[bot] = {t for t in self.__tasks[bot] if not t.done()}

        return Response(status=200)

    async def start(self):
        """

        :return:
        """

        if self.__started:
            return

        self.__started = True

        logger.info("Starting with webhook...")

        runner = ServerRunner(Server(self.__handler))
        await runner.setup()
        self.__srv = TCPSite(runner, self.__host, self.__port)

        logger.info("Listening on http://%s:%s%s", self.__host, self.__port, self.__base_path)

        await self.__srv.start()

        logger.info("Running!")

    @staticmethod
    async def __wait_tasks(tasks: Set[asyncio.Task]):
        while len(tasks):
            logger.info("Waiting %s tasks...", len(tasks))
            _, tasks = await asyncio.wait(tasks, timeout=1, return_when=asyncio.FIRST_COMPLETED)

    async def stop(self):
        """

        :return:
        """
        logger.info("Stopping server...")

        if not self.__started:
            return

        self.__started = False

        if self.__srv:
            await self.__srv.stop()
            self.__srv = None

        tasks = set()
        for b, t in self.__tasks.items():
            tasks.update(t)
            t.clear()

        await self.__wait_tasks(tasks)

        logger.info("Stopped.")

    @classmethod
    def run(cls, bots: Union['Bot', List['Bot']], base_url: str, base_path: str, *, host: str = 'localhost',
            port: int = 8080, webhook_setup: bool = True, webhook_remove: bool = True,
            allowed_updates: Optional[List[UpdateType]] = None, drop_pending_updates: bool = False,
            signals: tuple = (signal.SIGINT, signal.SIGTERM), shutdown_wait: int = 10):
        """

        :param bots:
        :param base_url:
        :param base_path:
        :param host:
        :param port:
        :param webhook_setup:
        :param webhook_remove:
        :param allowed_updates:
        :param drop_pending_updates:
        :param signals:
        :param shutdown_wait:

        :return: None
        """

        executor = cls(base_url, base_path, host=host, port=port)

        def add(bot: 'Bot'):
            return executor.add_bot(bot, allowed_updates=allowed_updates, drop_pending_updates=drop_pending_updates,
                                    set_webhook=webhook_setup)

        def remove(bot: 'Bot'):
            return executor.remove_bot(bot, delete_webhook=webhook_remove)

        logger.info('Starting webhook executor...')
        logger.debug('Using base url: %s', base_url)
        logger.debug('Using base path: %s', base_path)

        cls._run(executor, add, remove, bots, signals, shutdown_wait=shutdown_wait)
