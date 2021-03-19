# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from enum import auto

from .utils import EnumAutoName


class EntityType(EnumAutoName):
    mention = auto()
    hashtag = auto()
    cashtag = auto()
    bot_command = auto()
    url = auto()
    email = auto()
    phone_number = auto()
    bold = auto()
    italic = auto()
    underline = auto()
    strikethrough = auto()
    code = auto()
    pre = auto()
    text_link = auto()
    text_mention = auto()
    unknown = auto()
