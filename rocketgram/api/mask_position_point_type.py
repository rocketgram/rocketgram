# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from enum import auto

from .utils import EnumAutoName


class MaskPositionPointType(EnumAutoName):
    forehead = auto()
    eyes = auto()
    mouth = auto()
    chin = auto()
