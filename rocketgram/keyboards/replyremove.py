# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).


class ReplyKeyboardRemove:
    def __init__(self, *, selective=False):
        self.set_selective(selective)

    def set_selective(self, selective=False):
        self.__selective = selective
        return self

    def render(self):
        keyboard = {'remove_keyboard': True}
        if self.__selective:
            keyboard['selective'] = True
        return keyboard
