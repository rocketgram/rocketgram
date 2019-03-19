# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).

import asyncio
import logging
import signal
from contextlib import suppress
from typing import TYPE_CHECKING, Set, Dict

try:
    import ujson as json
except ModuleNotFoundError:
    import json

from aiohttp import web

from .executor import Executor
from ..errors import TelegramSendError

if TYPE_CHECKING:
    from ..bot import Bot

logger = logging.getLogger('rocketgram.executors.webhook')


class WebHooksExecutor(Executor):
    def __init__(self, base_url: str, base_path: str, *, detached: bool = False, host: str = 'localhost',
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
        self.__detached = False

        self.__tasks: Dict[Bot, Set[asyncio.Task]] = dict()

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

    async def add_bot(self, bot: 'Bot', *, suffix=None, webhook=True, drop_updates=False,
                      max_connections=None):
        """

        :param bot:
        :param suffix:
        :param webhook:
        :param drop_updates:
        :param max_connections:
        """
        if bot in self.__bots.values():
            raise TypeError('Bot already added.')

        if not suffix:
            suffix = bot.token

        full_path = self.__base_path + suffix
        full_url = self.__base_url + suffix

        if bot.name is None:
            response = await bot.get_me()
            bot.name = response.result.username
            logger.info('Bot authorized as @%s', response.result.username)

        await bot.init()

        if drop_updates:
            await bot.delete_webhook()
            offset = 0
            while True:
                resp = await bot.get_updates(offset + 1)
                if not len(resp.result):
                    break
                for update in resp.result:
                    if offset < update.update_id:
                        offset = update.update_id
            logger.debug('Updates dropped for @%s', bot.name)

        self.__bots[full_path] = bot
        logger.info('Added bot @%s', bot.name)

        if webhook or drop_updates:
            await bot.set_webhook(full_url, max_connections=max_connections)
            logger.debug('Webhook setup done for bot @%s', bot.name)

    async def remove_bot(self, bot: 'Bot', webhook=True):
        """

        :param bot:
        :param webhook:
        """
        if bot not in self.__bots.values():
            raise TypeError('Bot was not found.')

        self.__bots = {k: v for k, v in self.__bots.items() if v != bot}

        if bot in self.__tasks:
            tasks = self.__tasks[bot]
            self.__tasks[bot] = set()
            await self.__wait_tasks(tasks)

        if webhook:
            try:
                await bot.delete_webhook()
            except TelegramSendError:
                logger.error('Error while removing webhook for %s.' % bot.name)

        await bot.shutdown()

        logger.info('Removed bot @%s', bot.name)

    async def start(self):
        """

        :return:
        """

        async def __handler(request: web.BaseRequest):
            if request.method != 'POST':
                return web.Response(status=400, text="Bad request.")

            bot: 'Bot' = self.__bots.get(request.path)

            if not bot:
                logger.warning("Bot not found for request '%s %s'.", request.method, request.path)
                return web.Response(status=404, text="Not found.")

            if not bot in self.__tasks:
                self.__tasks[bot] = set()

            task = asyncio.create_task(
                bot.process(await request.read(), webhook=not self.__detached, webhook_sendfile=False))
            self.__tasks[bot].add(task)

            if self.__detached:
                return web.Response(status=200)

            response = await task
            if response:
                if response.send_file:
                    raise RuntimeError('Sending files though webhook-request not supported!')

                data = json.dumps(response.request)
                return web.Response(body=data, headers={'Content-Type': 'application/json'})

            self.__tasks[bot] = {t for t in self.__tasks[bot] if not t.done()}

            return web.Response()

        if self.__started:
            return

        self.__started = True

        logger.info("Starting with webhooks...")

        loop = asyncio.get_event_loop()

        logger.info("Listening on http://%s:%s%s", self.__host, self.__port, self.__base_path)
        self.__srv = await loop.create_server(web.Server(__handler), self.__host, self.__port, backlog=128)

        logger.info("Running!")

    async def __wait_tasks(self, tasks: Set[asyncio.Task]):
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


def run_webhook(bots, base_url: str, base_path: str, *, host='0.0.0.0', port=8080, webhook_setup=True,
                webhook_delete=True, drop_updates=False, signals: tuple = (signal.SIGINT,), shutdown_wait=3):
    """

    :param bots:
    :param base_url:
    :param base_path:
    :param host:
    :param port:
    :param webhook_setup:
    :param webhook_delete:
    :param drop_updates:
    :param signals:
    :param shutdown_wait:
    """

    # try to use uvloop
    with suppress(ModuleNotFoundError):
        import uvloop
        uvloop.install()

    logger.info('Starting webhook executor...')
    logger.debug('Using base url: %s', base_url)
    logger.debug('Using base path: %s', base_path)

    executor = WebHooksExecutor(base_url, base_path, host=host, port=port)
    loop = asyncio.get_event_loop()

    if not isinstance(bots, (list, tuple)):
        bots = (bots,)

    async def run():
        for bot in bots:
            await executor.add_bot(bot, webhook=webhook_setup, drop_updates=drop_updates)
        await executor.start()

    async def stop():
        await executor.stop()
        for bot in executor.bots:
            await executor.remove_bot(bot, webhook=webhook_delete)

    loop.run_until_complete(run())

    for s in signals:
        loop.add_signal_handler(s, loop.stop)

    loop.run_forever()

    for s in signals:
        loop.remove_signal_handler(s)

    logger.info('Shutting down...')

    loop.run_until_complete(stop())

    pending = asyncio.Task.all_tasks()
    waits = asyncio.wait_for(asyncio.shield(asyncio.gather(*pending)), shutdown_wait)

    with suppress(asyncio.TimeoutError):
        loop.run_until_complete(waits)

    pending = asyncio.Task.all_tasks()
    for t in pending:
        if not t.done():
            logger.error('Cancelled pending task during shutdown: %s', t)
            t.cancel()

    with suppress(asyncio.CancelledError):
        loop.run_until_complete(asyncio.gather(*pending))

    logger.info('Bye!')
