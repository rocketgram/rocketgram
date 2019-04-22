# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).


import io
from enum import Enum

API_URL = "https://api.telegram.org/bot%s/"
API_FILE_URL = "https://api.telegram.org/file/bot%s/"


class InputFile:
    """\
    Represents InputFile request object:
    https://core.telegram.org/bots/api#inputfile
    """

    def __init__(self, file_name: str, content_type: str, data: io.IOBase):
        self.__file_name = file_name
        self.__content_type = content_type
        self.__data = data

    @property
    def file_name(self) -> str:
        return self.__file_name

    @property
    def content_type(self) -> str:
        return self.__content_type

    @property
    def data(self) -> io.IOBase:
        return self.__data

    def __copy__(self):
        return self

    def __deepcopy__(self, memo):
        return self

    def __repr__(self):
        return "%s(%s, %s, %s)" % (self.__class__.__name__,
                                   repr(self.__file_name),
                                   repr(self.__content_type),
                                   repr(self.__data))


class EnumAutoName(Enum):
    """Class for enums."""

    def _generate_next_value_(name, start, count, last_values):
        return name
