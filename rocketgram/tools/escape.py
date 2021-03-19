# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


import re

MD_RE = re.compile(r"([*_`\[])")
MD2_RE = re.compile(r"([_*\[\]()~`>#+\-|{}.!])")


def html(text: str) -> str:
    """Helper function to escape html symbols"""

    return text.replace(u'&', u'&amp;').replace(u'<', u'&lt;').replace(u'>', u'&gt;')


def markdown(text: str) -> str:
    """Helper function to escape markdown symbols"""

    return MD_RE.sub(r'\\\1', text)


def markdown2(text: str) -> str:
    """Helper function to escape markdown2 symbols"""

    return MD2_RE.sub(r'\\\1', text)
