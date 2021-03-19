# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from io import FileIO, BytesIO
from typing import Union


class InputFile:
    """\
    Represents InputFile request object:
    https://core.telegram.org/bots/api#inputfile
    """

    __slots__ = ('__file_name', '__content_type', '__data')

    def __init__(self, file_name: str, content_type: str, data: Union[FileIO, BytesIO]):
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
    def data(self) -> Union[FileIO, BytesIO]:
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
