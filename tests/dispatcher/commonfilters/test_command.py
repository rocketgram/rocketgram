# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


import asyncio
from logging import getLogger
from typing import Tuple

import pytest

from rocketgram import Bot, Update, Dispatcher, Connector
from rocketgram import context as ctx
from rocketgram.routers.dispatcher import commonfilters

logger = getLogger(__name__)


def make_bot(bot_name: str = "TestBot") -> Tuple[Bot, Dispatcher]:
    connector = Connector()
    dispatcher = Dispatcher()
    bot = Bot("1234567890:AAgLHoRpZxIcND0EqNL15HurLzwwSKomngX", router=dispatcher, connector=connector)
    bot.name = bot_name

    return bot, dispatcher


def make_update(text: str):
    return Update.parse(
        {
            "update_id": 123456789,
            "message": {
                "message_id": 1234567,
                "from": {
                    "id": 123456789,
                    "is_bot": False,
                    "first_name": "User",
                    "username": "username",
                    "language_code": "en",
                    "is_premium": True
                },
                "chat": {
                    "id": 123456789,
                    "first_name": "User",
                    "username": "username",
                    "type": "private"
                },
                "date": 1691234567,
                "text": text
            }
        }
    )


@pytest.mark.dispatcher
def test_command():
    bot, dispatcher = make_bot()

    results = []

    @dispatcher.handler
    @commonfilters.command("/start")
    async def handler():
        results.append(ctx.update)

    update_expected_1 = make_update("/start")
    update_expected_2 = make_update("/start@TestBot")
    update_unexpected_1 = make_update("/start@UnknownBot")
    update_unexpected_2 = make_update("/stop")

    asyncio.run(bot.process(None, update_expected_1))
    asyncio.run(bot.process(None, update_expected_2))
    asyncio.run(bot.process(None, update_unexpected_1))
    asyncio.run(bot.process(None, update_unexpected_2))

    assert update_expected_1 in results
    assert update_expected_2 in results
    assert update_unexpected_1 not in results
    assert update_unexpected_2 not in results

    assert len(results) == 2
