# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).

import asyncio
import logging
import signal
import typing
from contextlib import suppress

from .executor import Executor

if typing.TYPE_CHECKING:
    from ..bot import Bot

logger = logging.getLogger('rocketgram.executors.updates')


class UpdatesExecutor(Executor):
    def __init__(self, request_timeout=30):
        """

        """
        self.__timeout = request_timeout

        self.__bots: typing.List['Bot'] = list()
        self.__task = None
        self.__started = False

    @property
    def bots(self) -> typing.List['Bot']:
        """

        :return:
        """
        return self.__bots.copy()

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

        self.__bots.append(bot)

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

    async def remove_bot(self, bot: 'Bot'):
        """

        :param bot:
        """
        if bot not in self.__bots:
            raise TypeError('Bot was not found.')

        self.__bots.remove(bot)

        await bot.shutdown()

    async def start(self):
        """

        :return:
        """

        if self.__started:
            return

        async def __run():

            offsets = dict()
            running = list()

            async def __process(bot):
                upds = list()
                resp = await bot.get_updates(offsets.get(bot, 0) + 1, timeout=self.__timeout)
                for update in resp.result:
                    if offsets.get(bot, 0) < update.update_id:
                        offsets[bot] = update.update_id

                    upds.append(bot.process(update))

                await asyncio.gather(*upds)

                return bot

            pending = set()

            try:
                while True:
                    for bot in self.__bots:
                        if bot not in running:
                            running.append(bot)
                            pending.add(asyncio.create_task(__process(bot)))

                    if len(pending):
                        done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)

                        for d in done:
                            running.remove(d.result())
                    else:
                        logger.info("Nothing to run. Sleep some time...")
                        await asyncio.sleep(1)

            except asyncio.CancelledError:
                for t in pending:
                    t.cancel()
                    with suppress(asyncio.CancelledError):
                        await t

        logger.info("Starting with updates...")

        self.__started = True
        self.__task = asyncio.get_event_loop().create_task(__run())

        logger.info("Running!")

    async def stop(self):
        """

        :return:
        """

        if not self.__started:
            return

        logger.info("Stopping server...")

        self.__started = False

        self.__task.cancel()
        with suppress(asyncio.CancelledError):
            await self.__task

        self.__task = None

        logger.info("Stopped.")


def run_updates(bots, drop_updates=False, signals: tuple = (signal.SIGINT,), shutdown_wait=5):
    """

    :param bots:
    :param drop_updates:
    :param signals:
    :param shutdown_wait:
    """
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
