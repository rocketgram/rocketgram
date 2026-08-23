# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from enum import auto

from .utils import EnumAutoName


class TransactionPartnerType(EnumAutoName):
    user = auto()
    chat = auto()
    affiliate_program = auto()
    fragment = auto()
    telegram_ads = auto()
    telegram_api = auto()
    other = auto()
    unknown = auto()
