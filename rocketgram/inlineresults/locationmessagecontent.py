# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).


class LocationMessageContent:
    """https://core.telegram.org/bots/api#inputlocationmessagecontent"""

    def __init__(self, latitude, longitude):
        self._data = dict()

        self._data['latitude'] = latitude
        self._data['longitude'] = longitude

    def render(self):
        return self._data
