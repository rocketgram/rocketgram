# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional

from .menu_button_commands import MenuButtonCommands
from .menu_button_default import MenuButtonDefault
from .menu_button_web_app import MenuButtonWebApp
from .request import Request
from .web_app_info import WebAppInfo
from ..context import context


@dataclass(frozen=True)
class GetChatMenuButton(Request):
    """\
    Represents GetChatMenuButton request object:
    https://core.telegram.org/bots/api#getchatmenubutton
    """

    chat_id: Optional[Union[int, str]] = None

    def parse_result(self, data) -> Union[MenuButtonCommands, MenuButtonDefault, MenuButtonWebApp]:
        assert isinstance(data, dict), "Should be dict."

        result_type = data['type']

        if result_type == MenuButtonCommands.type:
            return MenuButtonCommands()

        if result_type == MenuButtonWebApp.type:
            return MenuButtonWebApp(text=data['text'], web_app=WebAppInfo.parse(data['web_app']))

        return MenuButtonDefault()

    async def send(self) -> Union[MenuButtonCommands, MenuButtonDefault, MenuButtonWebApp]:
        res = await context.bot.send(self)

        return res.result
