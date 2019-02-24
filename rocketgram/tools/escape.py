# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).

import re


def html(text):
    """Helper function to escape rocketgram html symbols"""
    t = str(text)
    t = t.replace(u'&', u'&amp;')
    t = t.replace(u'<', u'&lt;')
    t = t.replace(u'>', u'&gt;')

    return t


def markdown(text):
    """Helper function to escape rocketgram markup symbols"""
    escape_chars = '\*_`\['
    return re.sub(r'([%s])' % escape_chars, r'\\\1', text)
