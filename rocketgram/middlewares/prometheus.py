# Copyright (C) 2015-2019 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


import logging
from contextlib import suppress

import prometheus_client as prometheus

from . import Middleware
from .. import Request, Response, RocketgramRequestError
from ..context import context2 as context

logger = logging.getLogger('rocketgram.middlewares.prometheusmiddleware')


class PrometheusMiddleware(Middleware):
    def __init__(self, registry: prometheus.CollectorRegistry = None):
        self.__registry = registry if registry else prometheus.REGISTRY

        self.__updates = prometheus.Counter('rocketgram_updates', 'Rocketgram received updates', ('bot', 'type'),
                                            registry=self.__registry)
        self.__process_errors = prometheus.Counter('rocketgram_process_errors', 'Rocketgram process errors',
                                                   ('bot', 'type'), registry=self.__registry)

        self.__requests = prometheus.Counter('rocketgram_requests', 'Rocketgram sent requests', ('bot', 'type'))
        self.__request_errors = prometheus.Counter('rocketgram_request_errors', 'Rocketgram sent request errors',
                                                   ('bot', 'type', 'code'), registry=self.__registry)

        self.__bots = prometheus.Gauge('rocketgram_bots', 'Rocketgram active bots', registry=self.__registry)

    @property
    def registry(self) -> prometheus.CollectorRegistry:
        return self.__registry

    def init(self):
        self.__bots.inc()

    def shutdown(self):
        self.__bots.dec()

    def before_process(self):
        self.__updates.labels(bot=context.bot().name, type=context.update().update_type.name).inc()

    async def after_process(self):
        pass

    def process_error(self, error: Exception):
        self.__process_errors.labels(bot=context.bot().name, type=context.update().update_type.name).inc()

    def before_request(self, request: 'Request') -> 'Request':
        bot = None

        with suppress(LookupError):
            bot = context.bot().name

        self.__requests.labels(bot=bot, type=request.method).inc()
        return request

    def after_request(self, request: 'Request', response: 'Response') -> 'Response':
        return response

    def request_error(self, request: 'Request', error: Exception):
        code = None
        bot = None

        with suppress(LookupError):
            bot = context.bot().name

        if isinstance(error, RocketgramRequestError):
            code = error.response.code

        self.__request_errors.labels(bot=bot, type=request.method, code=code).inc()
