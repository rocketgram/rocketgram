# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


import asyncio
import logging
import signal
from typing import TYPE_CHECKING, Union, Dict, List, Set

from aiohttp import web

from .executor import Executor
from ..api import Request, GetMe, SetWebhook, DeleteWebhook
from ..api import Update
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
    def __init__(self, base_url: str, base_path: str, *, host: str = 'localhost',
                 port: int = 8080):
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

    async def add_bot(self, bot: 'Bot', *, suffix=None, set_webhook=True, drop_pending_updates=False,
                      max_connections=None):
        """

        :param bot:
        :param suffix:
        :param set_webhook:
        :param drop_pending_updates:
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
            await bot.send(SetWebhook(full_url, drop_pending_updates=drop_pending_updates,
                                      max_connections=max_connections))
            logger.debug('Webhook setup done for bot @%s', bot.name)

        if drop_pending_updates:
            logger.debug('Updates dropped for @%s', bot.name)

    async def remove_bot(self, bot: 'Bot', delete_webhook=True):
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

    async def start(self):
        """

        :return:
        """

        async def __handler(request: web.BaseRequest):
            if request.method != 'POST':
                return web.Response(status=400, text="Bad request.", headers=HEADERS_ERROR)

            bot = self.__bots.get(request.path)

            if not bot:
                logger.warning("Bot not found for request `%s`.", request.path)
                return web.Response(status=404, text="Not found.", headers=HEADERS_ERROR)

            if bot not in self.__tasks:
                self.__tasks[bot] = set()

            try:
                parsed = Update.parse(json.loads(await request.read()))
            except Exception:  # noqa
                logger.exception("Got exception while parsing update:")
                return web.Response(status=500, text="Server error.", headers=HEADERS_ERROR)

            task = asyncio.create_task(
                bot.process(self, parsed))
            self.__tasks[bot].add(task)

            try:
                response: Request = await task
            except Exception:  # noqa
                logger.exception("Got exception while processing update:")
                return web.Response(status=500, text="Server error.", headers=HEADERS_ERROR)

            if response:
                data = json.dumps(response.render(with_method=True))
                return web.Response(body=data, headers=HEADERS)

            self.__tasks[bot] = {t for t in self.__tasks[bot] if not t.done()}

            return web.Response(status=200)

        if self.__started:
            return

        self.__started = True

        logger.info("Starting with webhook...")

        loop = asyncio.get_event_loop()

        logger.info("Listening on http://%s:%s%s", self.__host, self.__port, self.__base_path)
        self.__srv = await loop.create_server(web.Server(__handler), self.__host, self.__port, backlog=128)

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
            self.__srv.close()
            await self.__srv.wait_closed()
            self.__srv = None

        tasks = set()
        for b, t in self.__tasks.items():
            tasks.update(t)
            t.clear()

        await self.__wait_tasks(tasks)

        logger.info("Stopped.")

    @classmethod
    def run(cls, bots: Union['Bot', List['Bot']], base_url: str, base_path: str, *, host='localhost', port=8080,
            webhook_setup=True, webhook_remove=True, drop_pending_updates=False,
            signals: tuple = (signal.SIGINT, signal.SIGTERM), shutdown_wait=10):
        """

        :param bots:
        :param base_url:
        :param base_path:
        :param host:
        :param port:
        :param webhook_setup:
        :param webhook_remove:
        :param drop_pending_updates:
        :param signals:
        :param shutdown_wait:

        :return: None
        """

        executor = cls(base_url, base_path, host=host, port=port)

        def add(bot: 'Bot'):
            return executor.add_bot(bot, set_webhook=webhook_setup, drop_pending_updates=drop_pending_updates)

        def remove(bot: 'Bot'):
            return executor.remove_bot(bot, delete_webhook=webhook_remove)

        logger.info('Starting webhook executor...')
        logger.debug('Using base url: %s', base_url)
        logger.debug('Using base path: %s', base_path)

        cls._run(executor, add, remove, bots, signals, shutdown_wait=shutdown_wait)
