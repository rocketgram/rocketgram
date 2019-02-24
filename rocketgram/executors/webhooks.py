# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).


import asyncio
import logging
import signal
from collections import namedtuple
from random import choice
from string import ascii_letters, digits

from aiohttp import web

from ..exceptions import TelegramSendError

logger = logging.getLogger('rocketgram.executors.webhook')

BotParams = namedtuple('BotParams', ('bot', 'url', 'path'))
HandlerParams = namedtuple('HandlerParams', ('method', 'path'))

SHUTDOWN_WAIT = 3
RANDOM_SUFFIX_LEN = 30


class WebHooksExecutor:
    def __init__(self, base_url, base_path, *, host=None, port=8080, skip_setup=False, skip_remove=False,
                 shutdown_signals=None):
        self.__bots = list()
        self.__handlers = dict()
        self.__base_url = base_url
        self.__base_path = base_path
        if not shutdown_signals:
            self.__shutdown_signals = (signal.SIGINT,)
        else:
            self.__shutdown_signals = shutdown_signals

        self.__skip_setup = skip_setup
        self.__skip_remove = skip_remove

        self.__srv = None
        self.__host = host
        self.__port = port

        self.__loop = asyncio.get_event_loop()

    def add_bot(self, bot, url=None, path=None, suffix=None):
        if url is None or path is None:
            if suffix is not None:
                url = self.__base_url + '/' + suffix
                path = self.__base_path + '/' + suffix
            else:
                rnd = ''.join([choice(ascii_letters + digits) for i in range(RANDOM_SUFFIX_LEN)])
                url = self.__base_url + '/' + rnd
                path = self.__base_path + '/' + rnd

        self.__bots.append(BotParams(bot, url, path))
        self.add_handler('POST', path, bot.process, is_bot=True)

    def add_handler(self, method, path, handler, is_bot=False):
        params = HandlerParams(method, path)
        if params in self.__handlers:
            raise ValueError('Duplicate handler params!')

        self.__handlers[params] = handler

    async def __webhandler(self, request: web.BaseRequest):
        params = HandlerParams(request.method, request.path)

        handler = self.__handlers.get(params)
        if not handler:
            logger.warning("Handler not found for request '%s %s'.", request.method, request.path)
            return web.Response(status=400, text="Bad request.")

        response = await handler(await request.read())
        if response:
            return web.Response(body=response, headers={'Content-Type': 'application/json'})

        return web.Response()

    def __signal(self, sig):
        logger.info("Got signal '%s'", sig)

        self.__loop.stop()

    async def init_bots(self):
        async def init(bot):
            try:
                await bot.init()
            except Exception:
                logger.exception('Error while init bot %s', bot.name)
                return False

            return True

        fs = [init(b.bot) for b in self.__bots]

        done, pending = await asyncio.wait(fs, loop=self.__loop)

        if False in [r.result() for r in done]:
            return False
        else:
            return True

    async def setup_webhooks(self):
        async def setup(bot, url):
            try:
                await bot.set_webhook(url)
            except TelegramSendError as error:
                logger.critical('setWebhook fail for @%s: %s, %s', bot.name, error.code, error.response.description)
                return False

            return True

        fs = [setup(b.bot, b.url) for b in self.__bots]

        done, pending = await asyncio.wait(fs, loop=self.__loop)

        if False in [r.result() for r in done]:
            return False
        else:
            return True

    async def remove_webhooks(self):
        async def remove(bot):
            try:
                await bot.delete_webhook()
            except TelegramSendError:
                logger.error('Error while removing webhook for %s.' % bot.name)

        await asyncio.gather(*[remove(b.bot) for b in self.__bots], loop=self.__loop)

    def run(self):
        logger.info("Starting with webhook...")

        loop = self.__loop

        if not loop.run_until_complete(self.init_bots()):
            self.shutdown(False)
            return

        webserver = web.Server(self.__webhandler)

        logger.info("Listening on http://%s:%s%s", self.__host, self.__port, self.__base_path)
        server = loop.create_server(webserver, self.__host, self.__port, backlog=128)

        if not self.__skip_setup:
            if not loop.run_until_complete(self.setup_webhooks()):
                self.shutdown()
                return

        self.__srv = loop.run_until_complete(server)

        logger.info("Running!")

        for sig in self.__shutdown_signals:
            loop.add_signal_handler(sig, self.__signal, sig)

        loop.run_forever()
        self.shutdown()

    def shutdown(self, remove_webhooks=True):
        logger.info("Shutting down...")

        loop = self.__loop

        if self.__srv:
            self.__srv.close()
            loop.run_until_complete(self.__srv.wait_closed())

        try:
            pending = asyncio.Task.all_tasks(loop=loop)
            waits = asyncio.wait_for(asyncio.shield(asyncio.gather(*pending)), SHUTDOWN_WAIT, loop=loop)
            loop.run_until_complete(waits)
        except asyncio.TimeoutError:
            pass

        pending = asyncio.Task.all_tasks(loop=loop)
        for t in asyncio.Task.all_tasks():
            if not t.done():
                logger.error('Cancelled pending task during shutdown: %s', t)
                t.cancel()
        try:
            loop.run_until_complete(asyncio.gather(*pending))
        except asyncio.CancelledError:
            pass  # skip error

        if not self.__skip_remove and remove_webhooks:
            loop.run_until_complete(self.remove_webhooks())

        shdwns = asyncio.gather(*[b.bot.shutdown() for b in self.__bots], loop=loop)
        loop.run_until_complete(shdwns)

        loop.close()

        logger.info("Done.")
