# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from enum import auto

from .utils import EnumAutoName


class ChatBoostSourceType(EnumAutoName):
    premium = auto()
    gift_code = auto()
    giveaway = auto()
    unknown = auto()
