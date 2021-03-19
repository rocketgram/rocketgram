# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


import asyncio
from inspect import isawaitable
import logging
from contextlib import suppress
from typing import List, Optional

from . import executors, routers, connectors, middlewares
from .api import Request, Response, Update
from .context import context
from .errors import RocketgramRequestError
from .errors import RocketgramStopRequest

logger = logging.getLogger('rocketgram.bot')
logger_raw_in = logging.getLogger('rocketgram.raw.in')
logger_raw_out = logging.getLogger('rocketgram.raw.out')


class Bot:
    __slots__ = ('__token', '__name', '__user_id', '__middlewares', '__router', '__own_connector', '__connector')

    def __init__(self, token: str, *, connector: 'connectors.Connector' = None, router: 'routers.Router' = None):
        """

        :param token: Bot's token
        :param connector: Connector object. If not specified Bot will try AioHttpConnector
        :param router: Router object. If not specified Bot will try Dispatcher
        """
        self.__token = token

        self.__name = None
        self.__user_id = int(self.__token.split(':')[0])
        self.__middlewares: List['middlewares.Middleware'] = list()

        self.__router = router
        if self.__router is None:
            from .routers.dispatcher import Dispatcher
            self.__router = Dispatcher()

        self.__own_connector = False
        self.__connector = connector

        if self.__connector is None:
            with suppress(ImportError):
                from .connectors import AioHttpConnector
                self.__own_connector = True
                self.__connector = AioHttpConnector()

        if self.__connector is None:
            with suppress(ImportError):
                from .connectors import TornadoConnector
                self.__own_connector = True
                self.__connector = TornadoConnector()

        if self.__connector is None:
            raise RuntimeError("Can't create Connector object. Tornado or AioHttp should be installed.")

    @property
    def token(self) -> str:
        """Bot's token."""

        return self.__token

    @property
    def name(self) -> str:
        """Bot's username. Can be set one time."""

        return self.__name

    @name.setter
    def name(self, name: str):
        if self.__name is not None:
            raise TypeError('Bot''s name can be set one time.')

        self.__name = name

    @property
    def user_id(self) -> int:
        """Bot's user_id."""

        return self.__user_id

    @property
    def router(self) -> 'routers.Router':
        """Bot's router."""

        return self.__router

    @property
    def connector(self) -> 'connectors.Connector':
        """Bot's connector."""

        return self.__connector

    def middleware(self, middleware: 'middlewares.Middleware'):
        """Registers middleware."""

        self.__middlewares.append(middleware)

    async def init(self):
        """Initializes connector and dispatcher.
        Performs bot initialization authorize bot on telegram and sets bot's name.

        Must be called before any operation with bot."""

        logger.debug('Performing init...')

        context.bot = self

        if self.__own_connector:
            await self.connector.init()

        await self.router.init()

        for mw in self.__middlewares:
            m = mw.init()
            if isawaitable(m):
                await m

        return True

    async def shutdown(self):
        """Release bot's resources.

        Must be called after bot work was done."""

        logger.debug('Performing shutdown...')

        context.bot = self

        await self.router.shutdown()

        for mw in reversed(self.__middlewares):
            m = mw.shutdown()
            if isawaitable(m):
                await m

        if self.__own_connector:
            await self.connector.shutdown()

    async def process(self, executor: 'executors.Executor', update: Update) -> Optional[Request]:
        logger_raw_in.debug('Raw in: %s', update.raw)

        context.assign(executor, self, update)

        try:
            for mw in self.__middlewares:
                m = mw.before_process()
                if isawaitable(m):
                    await m

            await self.router.process()

            webhook_request = None

            for req in context.webhook_requests:
                # set request to return if it can be processed
                if webhook_request is None and executor.can_process_webhook_request(req):
                    for mw in self.__middlewares:
                        req = mw.before_request(req)
                        if isawaitable(req):
                            req = await req
                    webhook_request = req
                    continue

                # fallback and send by hands
                with suppress(Exception):
                    await self.send(req)

            for mw in self.__middlewares:
                m = mw.after_process()
                if isawaitable(m):
                    await m

            return webhook_request

        except RocketgramStopRequest as e:
            logger.debug('Request `%s` was interrupted: `%s`', update.update_id, e)
        except asyncio.CancelledError:
            raise
        except Exception as error:
            for mw in self.__middlewares:
                with suppress(Exception):
                    m = mw.process_error(error)
                    if isawaitable(m):
                        await m

            logger.exception('Got exception during processing request:')

    async def send(self, request: Request) -> Response:
        try:
            for mw in self.__middlewares:
                request = mw.before_request(request)
                if isawaitable(request):
                    request = await request

            response = await self.__connector.send(self.token, request)

            for mw in reversed(self.__middlewares):
                response = mw.after_request(request, response)
                if isawaitable(response):
                    response = await response

            if response.ok:
                return response

            raise RocketgramRequestError.get_exception(request, response)

        except asyncio.CancelledError:
            raise
        except Exception as error:
            for mw in reversed(self.__middlewares):
                m = mw.request_error(request, error)
                if isawaitable(m):
                    await m
            raise
