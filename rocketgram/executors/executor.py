# Copyright (C) 2015-2019 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


import asyncio
import logging
import signal
from contextlib import suppress
from typing import TYPE_CHECKING, Callable, Union, List

from ..requests import Request

if TYPE_CHECKING:
    from ..bot import Bot

logger = logging.getLogger('rocketgram.executors.updates')


class Executor:
    @property
    def bots(self) -> List['Bot']:
        raise NotImplementedError

    @property
    def running(self) -> bool:
        raise NotImplementedError

    def can_process_webhook_request(self, request: Request) -> bool:
        raise NotImplementedError

    async def add_bot(self, bot: 'Bot', *, drop_updates=False):
        raise NotImplementedError

    async def remove_bot(self, bot: 'Bot'):
        raise NotImplementedError

    async def start(self):
        raise NotImplementedError

    async def stop(self):
        raise NotImplementedError

    @staticmethod
    def _run(executor: 'Executor', add: Callable, remove: Callable, bots: Union['Bot', List['Bot']],
             signals: tuple = (signal.SIGINT, signal.SIGTERM), shutdown_wait=10):
        """

        :param bots:
        :param add:
        :param remove:
        :param signals:
        :param shutdown_wait:
        """

        loop = asyncio.get_event_loop()

        if not isinstance(bots, (list, tuple)):
            bots = (bots,)

        async def run():
            for bot in bots:
                await add(bot)
            await executor.start()

        async def stop():
            await executor.stop()
            for bot in executor.bots:
                await remove(bot)

        loop.run_until_complete(run())

        for s in signals:
            try:
                loop.add_signal_handler(s, loop.stop)
            except NotImplementedError:
                signal.signal(s, lambda sig, frame: loop.stop())

        loop.run_forever()

        with suppress(NotImplementedError):
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
