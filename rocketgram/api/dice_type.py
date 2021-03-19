# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from enum import Enum


class DiceType(Enum):
    """\
    Type for dice object:

    https://core.telegram.org/bots/api#senddice
    https://core.telegram.org/bots/api#dice
    """

    dice = "🎲"
    darts = "🎯"
    basketball = "🏀"
    football = "⚽"
    bowling = "🎳"
    slot_machine = "🎰"
    unknown = "unknown"
