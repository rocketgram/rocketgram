# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


import asyncio
import logging
from secrets import compare_digest

from aiohttp.web import Server, ServerRunner, BaseRequest, TCPSite, Response

from .webhook import WebhookExecutor
from ..api import Request, Update

logger = logging.getLogger('rocketgram.executors.aiohttp')


class AioHttpExecutor(WebhookExecutor):
    __slots__ = ()

    async def __handler(self, request: BaseRequest):
        if request.method != 'POST':
            return Response(status=400, text="Bad request.", headers=self.HEADERS_ERROR)

        bot = self._bots.get(request.path)

        if not bot:
            logger.warning("Bot not found for request `%s`.", request.path)
            return Response(status=404, text="Not found.", headers=self.HEADERS_ERROR)

        token = self._secret_tokens.get(bot)

        if token and not compare_digest(token, request.headers.get(self.HEADER_SECRET, '')):
            logger.warning("Wrong token was provided for the bot `%s`.", bot.name)
            return Response(status=403, text="Wrong token.", headers=self.HEADERS_ERROR)

        try:
            parsed = Update.parse(self._loads(await request.read()))
        except Exception:  # noqa
            logger.exception("Got exception while parsing update:")
            return Response(status=500, text="Server error.", headers=self.HEADERS_ERROR)

        task = asyncio.create_task(bot.process(self, parsed))
        self._tasks[bot].add(task)

        try:
            response: Request = await task
        except Exception:  # noqa
            logger.exception("Got exception while processing update:")
            return Response(status=500, text="Server error.", headers=self.HEADERS_ERROR)

        if response:
            data = self._dumps(response.render(with_method=True))
            return Response(body=data, headers=self.HEADERS)

        self._tasks[bot] = {t for t in self._tasks[bot] if not t.done()}

        return Response(status=200)

    async def start(self):
        if self._started:
            return

        self._started = True

        logger.info("Starting with webhook...")

        runner = ServerRunner(Server(self.__handler))
        await runner.setup()
        self._srv = TCPSite(runner, self._host, self._port)

        logger.info("Listening on http://%s:%s%s", self._host, self._port, self._base_path)

        await self._srv.start()

        logger.info("Running!")

    async def stop(self):
        logger.info("Stopping server...")

        if not self._started:
            return

        self._started = False

        if self._srv:
            await self._srv.stop()
            self._srv = None

        tasks = set()
        for b, t in self._tasks.items():
            tasks.update(t)
            t.clear()

        await self._wait_tasks(tasks)

        logger.info("Stopped.")
