﻿# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


import re

MD_RE = re.compile(r"([*_`\[])")
MD2_RE = re.compile(r"([_*\[\]()~`>#+\-=|{}.!\\])")


def html(text: str) -> str:
    """Helper function to escape html symbols"""

    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def markdown(text: str) -> str:
    """Helper function to escape markdown symbols"""

    return MD_RE.sub(r'\\\1', text)


def markdown2(text: str) -> str:
    """Helper function to escape markdown2 symbols"""

    return MD2_RE.sub(r'\\\1', text)
