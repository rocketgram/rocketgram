# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass


@dataclass(frozen=True)
class InlineQueryResult:
    """\
    Represents InlineQueryResult object:
    https://core.telegram.org/bots/api#inlinequeryresult
    """
