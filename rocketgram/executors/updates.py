# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).


import asyncio
import logging
import typing

if typing.TYPE_CHECKING:
    from ..bot import Bot

logger = logging.getLogger('rocketgram.executors.updates')


class UpdatesExecutor():
    def __init__(self, timeout=30, delete_webhook=True):
        self.__bots = list()
        self.__loop = asyncio.get_event_loop()
        self.__timeout = timeout

    def add_bot(self, bot: 'Bot'):
        self.__bots.append(bot)

    async def init_bots(self):
        async def init(bot):
            try:
                await bot.init()
            except Exception:
                logger.exception('Error while init router %s', bot.name)
                return False

            return True

        fs = [init(bot) for bot in self.__bots]

        done, pending = await asyncio.wait(fs, loop=self.__loop)

        if False in [r.result() for r in done]:
            return False
        else:
            return True

    async def run_updates(self):
        async def process(bot):
            await bot.delete_webhook()

            offset = 0
            while True:
                upds = list()
                resp = await bot.get_updates(offset + 1, timeout=self.__timeout)
                for update in resp.result:
                    if offset < update.update_id:
                        offset = update.update_id

                    upds.append(bot.process(update))

                await asyncio.gather(*upds, loop=self.__loop)

        await asyncio.wait([process(bot) for bot in self.__bots], loop=self.__loop)

    def run(self):
        logger.info("Starting router with updates...")

        loop = self.__loop

        if not loop.run_until_complete(self.init_bots()):
            self.shutdown()
            return

        logger.info("Running!")

        try:
            loop.run_until_complete(self.run_updates())
        except KeyboardInterrupt:  # pragma: no cover
            pass
        finally:
            self.shutdown()

    def shutdown(self):
        logger.info("Shutting down...")

        loop = self.__loop

        shdwns = asyncio.gather(*[bot.init() for bot in self.__bots], loop=loop)
        loop.run_until_complete(shdwns)

        loop.close()

        logger.info("Done.")
