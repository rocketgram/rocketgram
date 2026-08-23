# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from enum import auto

from .utils import EnumAutoName


class RevenueWithdrawalStateType(EnumAutoName):
    pending = auto()
    succeeded = auto()
    failed = auto()
    unknown = auto()
