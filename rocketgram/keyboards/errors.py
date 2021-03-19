# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from ..errors import RocketgramError


class TooManyButtonsError(RocketgramError):
    pass


class NotEnoughButtonsError(RocketgramError):
    pass
