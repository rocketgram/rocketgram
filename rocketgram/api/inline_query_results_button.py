# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .web_app_info import WebAppInfo


@dataclass(frozen=True)
class InlineQueryResultsButton:
    """\
    Represents InlineQueryResultsButton object:
    https://core.telegram.org/bots/api#inlinequeryresultsbutton
    """

    text: str
    web_app: Optional[WebAppInfo] = None
    start_parameter: Optional[str] = None
