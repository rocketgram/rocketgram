# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass

from .. import api
from ..context import context
from .keyboard_button import KeyboardButton
from .request import Request


@dataclass(frozen=True)
class SavePreparedKeyboardButton(Request):
    """\
    Represents SavePreparedKeyboardButton request object:
    https://core.telegram.org/bots/api#savepreparedkeyboardbutton
    """

    user_id: int
    button: KeyboardButton

    def parse_result(self, data) -> 'api.PreparedKeyboardButton':
        assert isinstance(data, dict), "Should be dict."
        return api.PreparedKeyboardButton.parse(data)

    async def send(self) -> 'api.PreparedKeyboardButton':
        res = await context.bot.send(self)
        return res.result
