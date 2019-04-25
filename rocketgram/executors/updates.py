# Copyright (C) 2015-2019 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


import asyncio
import logging
import signal
from typing import TYPE_CHECKING, Union, Optional, Dict, List, Set

from .executor import Executor
from ..errors import RocketgramNetworkError
from ..requests import Request, GetMe, GetUpdates, DeleteWebhook

if TYPE_CHECKING:
    from ..bot import Bot

logger = logging.getLogger('rocketgram.executors.updates')


class UpdatesExecutor(Executor):
    def __init__(self, request_timeout=30):
        """

        """

        self.__timeout = request_timeout

        self.__bots: Dict['Bot', Optional[asyncio.Task]] = dict()
        self.__task = None
        self.__started = False

    @property
    def bots(self) -> List['Bot']:
        """

        :return:
        """
        return list(self.__bots.keys())

    @property
    def running(self) -> bool:
        """

        :rtype: object
        """
        return self.__started

    def can_process_webhook_request(self, request: Request) -> bool:
        return False

    async def add_bot(self, bot: 'Bot', *, drop_updates=False):
        """

        :param bot:
        :param drop_updates:
        """
        if bot in self.__bots:
            raise ValueError('Bot already added.')

        if bot.name is None:
            response = await bot.send(GetMe())
            bot.name = response.result.username
            logger.info('Bot authorized as @%s', response.result.username)

        await bot.init()

        logger.info('Added bot @%s', bot.name)

        self.__bots[bot] = None

        await bot.send(DeleteWebhook())

        if drop_updates:
            offset = 0
            while True:
                resp = await bot.send(GetUpdates(offset + 1))
                if not len(resp.result):
                    break
                for update in resp.result:
                    if offset < update.update_id:
                        offset = update.update_id
            logger.debug('Updates dropped for @%s', bot.name)

        if self.running:
            self.__start_bot(bot)

    async def remove_bot(self, bot: 'Bot'):
        """

        :param bot:
        """
        if bot not in self.__bots:
            raise ValueError('Bot was not found.')

        tasks = self.__bots[bot]
        del self.__bots[bot]

        if tasks:
            await self.__wait_tasks({tasks})

        await bot.shutdown()

        logger.info('Removed bot @%s', bot.name)

    async def __runner(self, bot: 'Bot') -> Set[asyncio.Task]:
        offset = 0
        pending = set()
        while True:
            try:
                resp = await bot.send(GetUpdates(offset + 1, timeout=self.__timeout))
                for update in resp.result:
                    if offset < update.update_id:
                        offset = update.update_id

                    task = asyncio.create_task(bot.process(self, update))
                    task.done()
                    pending.add(task)

                pending = {t for t in pending if not t.done()}
            except RocketgramNetworkError:
                logging.exception('Exception while processing updates')
            except asyncio.CancelledError:
                return pending
            except:
                logging.exception('Exception while processing updates')

    def __start_bot(self, bot: 'Bot'):
        assert bot in self.__bots, 'Unknown bot!'
        assert self.__bots[bot] is None, 'Bot already started!'

        aw = self.__runner(bot)
        task = asyncio.create_task(aw)
        self.__bots[bot] = task

    async def start(self):
        """

        :return:
        """

        if self.__started:
            return
        self.__started = True

        logger.info("Starting with updates...")

        for bot in self.__bots:
            self.__start_bot(bot)

        logger.info("Running!")

    async def __wait_tasks(self, tasks: Set[asyncio.Task]):
        pending = set()
        for task in tasks:
            task.cancel()
            p = await task
            pending.update(p)

        while len(pending):
            logger.info("Waiting %s tasks...", len(pending))
            _, pending = await asyncio.wait(pending, timeout=1, return_when=asyncio.FIRST_COMPLETED)

    async def stop(self):
        """

        :return:
        """

        if not self.__started:
            return

        self.__started = False

        logger.info("Stopping server...")

        tasks = set()
        for bot, task in self.__bots.items():
            self.__bots[bot] = None
            if task:
                tasks.add(task)

        await self.__wait_tasks(tasks)

        logger.info("Stopped.")

    @classmethod
    def run(cls, bots: Union['Bot', List['Bot']], *, drop_updates=False,
            signals: tuple = (signal.SIGINT, signal.SIGTERM),
            request_timeout=30, shutdown_wait=10):
        """

        :param bots:
        :param drop_updates:
        :param signals:
        :param shutdown_wait:
        """

        executor = cls(request_timeout=request_timeout)

        def add(bot: 'Bot'):
            return executor.add_bot(bot, drop_updates=drop_updates)

        def remove(bot: 'Bot'):
            return executor.remove_bot(bot)

        logger.info('Starting updates executor...')

        cls._run(executor, add, remove, bots, signals, shutdown_wait=shutdown_wait)
