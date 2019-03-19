# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).

import asyncio
import logging
import signal
from contextlib import suppress
from typing import TYPE_CHECKING, Optional, Dict, List, Set

from .executor import Executor

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

    async def add_bot(self, bot: 'Bot', *, drop_updates=False):
        """

        :param bot:
        :param drop_updates:
        """
        if bot in self.__bots:
            raise TypeError('Bot already added.')

        if bot.name is None:
            response = await bot.get_me()
            bot.name = response.result.username
            logger.info('Bot authorized as @%s', response.result.username)

        await bot.init()

        logger.info('Added bot @%s', bot.name)

        self.__bots[bot] = None

        await bot.delete_webhook()

        if drop_updates:
            offset = 0
            while True:
                resp = await bot.get_updates(offset + 1)
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
            raise TypeError('Bot was not found.')

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
                resp = await bot.get_updates(offset + 1, timeout=self.__timeout)
                for update in resp.result:
                    if offset < update.update_id:
                        offset = update.update_id

                    task = asyncio.create_task(bot.process(update))
                    task.done()
                    pending.add(task)

                pending = {t for t in pending if not t.done()}
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


def run_updates(bots, drop_updates=False, signals: tuple = (signal.SIGINT,), shutdown_wait=5):
    """

    :param bots:
    :param drop_updates:
    :param signals:
    :param shutdown_wait:
    """

    # try to use uvloop
    with suppress(ModuleNotFoundError):
        import uvloop
        uvloop.install()

    logger.info('Starting updates executor...')

    executor = UpdatesExecutor()
    loop = asyncio.get_event_loop()

    if not isinstance(bots, (list, tuple)):
        bots = (bots,)

    async def run():
        for bot in bots:
            await executor.add_bot(bot, drop_updates=drop_updates)
        await executor.start()

    async def stop():
        await executor.stop()
        for bot in executor.bots:
            await executor.remove_bot(bot)

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

    with suppress(asyncio.CancelledError, asyncio.TimeoutError):
        loop.run_until_complete(asyncio.gather(*pending))

    logger.info('Bye!')
