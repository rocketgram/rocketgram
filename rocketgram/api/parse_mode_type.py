# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from enum import auto

from .utils import EnumAutoName


class ParseModeType(EnumAutoName):
    """\
    Formatting options type:
    https://core.telegram.org/bots/api#formatting-options
    """

    html = auto()
    markdown = auto()
    markdownv2 = auto()
