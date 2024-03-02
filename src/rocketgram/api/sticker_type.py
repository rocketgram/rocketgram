# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from enum import auto

from .utils import EnumAutoName


class StickerType(EnumAutoName):
    regular = auto()
    mask = auto()
    custom_emoji = auto()
    unknown = auto()
