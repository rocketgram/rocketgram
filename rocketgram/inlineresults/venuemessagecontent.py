# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).


class VenueMessageContent:
    """https://core.telegram.org/bots/api#inputvenuemessagecontent"""

    def __init__(self, latitude, longitude, title, address, foursquare_id=None):
        self._data = dict()

        self._data['latitude'] = latitude
        self._data['longitude'] = longitude
        self._data['title'] = title
        self._data['address'] = address
        if foursquare_id:
            self._data['foursquare_id'] = foursquare_id

    def render(self):
        return self._data
