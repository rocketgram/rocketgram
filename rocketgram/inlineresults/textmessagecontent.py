# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).


class TextMessageContent:
    """https://core.telegram.org/bots/api#inputtextmessagecontent"""

    def __init__(self, message_text, parse_mode=None, disable_web_page_preview=None):
        self._data = dict()

        self._data['message_text'] = message_text
        if parse_mode:
            self._data['parse_mode'] = parse_mode
        if disable_web_page_preview is not None:
            self._data['disable_web_page_preview'] = disable_web_page_preview

    def render(self):
        return self._data
