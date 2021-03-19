# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


import asyncio
import logging

from tornado.httpserver import HTTPServer
from tornado.httputil import HTTPServerRequest, HTTPHeaders, ResponseStartLine

from .webhook import WebhookExecutor
from ..api import Request, Update

try:
    import ujson as json
except ImportError:
    import json

logger = logging.getLogger('rocketgram.executors.tornado')


class TornadoExecutor(WebhookExecutor):
    def __handler(self, request: HTTPServerRequest):
        err_headers = HTTPHeaders(self.HEADERS_ERROR)
        headers = HTTPHeaders(self.HEADERS)

        async def handle():
            if request.method != 'POST':
                await request.connection.write_headers(ResponseStartLine('1.1', 400, 'Bad Request'), err_headers)
                await request.connection.write('Bad request.'.encode())
                request.connection.finish()
                return

            bot = self._bots.get(request.path)

            if not bot:
                logger.warning("Bot not found for request `%s`.", request.path)
                await request.connection.write_headers(ResponseStartLine('1.1', 404, 'Not Found'), err_headers)
                await request.connection.write('Not found.'.encode())
                request.connection.finish()
                return

            try:
                parsed = Update.parse(json.loads(request.body))
            except Exception:  # noqa
                logger.exception("Got exception while parsing update:")
                await request.connection.write_headers(ResponseStartLine('1.1', 500, 'Internal Server Error'),
                                                       err_headers)
                await request.connection.write('Server error.'.encode())
                request.connection.finish()
                return

            if bot not in self._tasks:
                self._tasks[bot] = set()

            task = asyncio.create_task(bot.process(self, parsed))
            self._tasks[bot].add(task)

            try:
                response: Request = await task
            except Exception:  # noqa
                logger.exception("Got exception while processing update:")
                await request.connection.write_headers(ResponseStartLine('1.1', 500, 'Internal Server Error'),
                                                       err_headers)
                await request.connection.write('Server error.'.encode())
                request.connection.finish()
                return

            await request.connection.write_headers(ResponseStartLine('1.1', 200, 'Ok'), headers)

            if response:
                data = json.dumps(response.render(with_method=True))
                await request.connection.write(data.encode())

            request.connection.finish()

            self._tasks[bot] = {t for t in self._tasks[bot] if not t.done()}

        asyncio.create_task(handle())

    async def start(self):
        if self._started:
            return

        self._started = True

        logger.info("Starting with webhook...")

        logger.info("Listening on http://%s:%s%s", self._host, self._port, self._base_path)

        self._srv = HTTPServer(self.__handler)
        self._srv.listen(self._port, address=self._host)

        logger.info("Running!")

    async def stop(self):
        logger.info("Stopping server...")

        if not self._started:
            return

        self._started = False

        if self._srv:
            self._srv.stop()
            await self._srv.close_all_connections()
            self._srv = None

        tasks = set()
        for b, t in self._tasks.items():
            tasks.update(t)
            t.clear()

        await self._wait_tasks(tasks)

        logger.info("Stopped.")
