# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


import asyncio
import logging
import signal
from typing import TYPE_CHECKING, Union, Optional, Dict, List, Set

from .executor import Executor
from ..api import GetMe, GetUpdates, DeleteWebhook, UpdateType
from ..errors import RocketgramNetworkError

if TYPE_CHECKING:
    from ..bot import Bot

logger = logging.getLogger('rocketgram.executors.updates')


class UpdatesExecutor(Executor):
    def __init__(self, request_timeout=30):
        self._timeout = request_timeout

        self._bots: Dict['Bot', Optional[asyncio.Task]] = dict()
        self._started = False

    @property
    def bots(self) -> List['Bot']:
        return list(self._bots.keys())

    @property
    def running(self) -> bool:
        return self._started

    async def add_bot(self, bot: 'Bot', *, allowed_updates: Optional[List[UpdateType]] = None,
                      drop_pending_updates: bool = False, **kwargs):

        assert not len(kwargs), "This method does not accept additional parameters!"

        if bot in self._bots:
            raise ValueError('Bot already added.')

        if bot.name is None:
            response = await bot.send(GetMe())
            bot.name = response.result.username
            logger.info('Bot authorized as @%s', response.result.username)

        await bot.init()

        logger.info('Added bot @%s', bot.name)

        self._bots[bot] = None

        await bot.send(DeleteWebhook(drop_pending_updates=drop_pending_updates))

        if drop_pending_updates:
            logger.debug('Updates dropped for @%s', bot.name)

        if self.running:
            self._start_bot(bot, allowed_updates=allowed_updates)

    async def remove_bot(self, bot: 'Bot'):
        if bot not in self._bots:
            raise ValueError('Bot was not found.')

        tasks = self._bots[bot]
        del self._bots[bot]

        if tasks:
            await self._wait_tasks({tasks})

        await bot.shutdown()

        logger.info('Removed bot @%s', bot.name)

    async def _runner(self, bot: 'Bot', allowed_updates: Optional[List[UpdateType]] = None) -> Set[asyncio.Task]:
        offset = 0
        pending = set()
        while True:
            try:
                resp = await bot.send(GetUpdates(offset + 1, allowed_updates=allowed_updates, timeout=self._timeout))
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
            except Exception:  # noqa
                logging.exception('Exception while processing updates')

    def _start_bot(self, bot: 'Bot', allowed_updates: Optional[List[UpdateType]] = None):
        assert bot in self._bots, 'Unknown bot!'
        assert self._bots[bot] is None, 'Bot already started!'

        task = asyncio.create_task(self._runner(bot, allowed_updates))
        self._bots[bot] = task

    async def start(self):
        if self._started:
            return
        self._started = True

        logger.info("Starting with updates...")

        for bot in self._bots:
            self._start_bot(bot)

        logger.info("Running!")

    @staticmethod
    async def _wait_tasks(tasks: Set[asyncio.Task]):
        pending = set()
        for task in tasks:
            task.cancel()
            p = await task
            pending.update(p)

        while len(pending):
            logger.info("Waiting %s tasks...", len(pending))
            _, pending = await asyncio.wait(pending, timeout=1, return_when=asyncio.FIRST_COMPLETED)

    async def stop(self):
        if not self._started:
            return

        self._started = False

        logger.info("Stopping server...")

        tasks = set()
        for bot, task in self._bots.items():
            self._bots[bot] = None
            if task:
                tasks.add(task)

        await self._wait_tasks(tasks)

        logger.info("Stopped.")

    @classmethod
    def run(cls, bots: Union['Bot', List['Bot']], *, allowed_updates: Optional[List[UpdateType]] = None,
            drop_pending_updates: bool = False, signals: tuple = (signal.SIGINT, signal.SIGTERM),
            request_timeout: int = 30, shutdown_wait: int = 10):

        executor = cls(request_timeout=request_timeout)

        def add(bot: 'Bot'):
            return executor.add_bot(bot, allowed_updates=allowed_updates, drop_pending_updates=drop_pending_updates)

        def remove(bot: 'Bot'):
            return executor.remove_bot(bot)

        logger.info('Starting updates executor...')

        cls._run(executor, add, remove, bots, signals, shutdown_wait=shutdown_wait)
