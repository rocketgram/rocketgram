# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).


class ContactMessageContent:
    """https://core.telegram.org/bots/api#inputcontactmessagecontent"""

    def __init__(self, phone_number, first_name, last_name=None):
        self._data = dict()

        self._data['phone_number'] = phone_number
        self._data['first_name'] = first_name
        if last_name:
            self._data['last_name'] = last_name

    def render(self):
        return self._data
