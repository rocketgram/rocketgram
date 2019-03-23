# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).


import typing
from dataclasses import dataclass
from enum import Enum


@dataclass(frozen=True)
class Default:
    """Default value indicator."""
    pass


@dataclass(frozen=True)
class InputFile:
    """Represents file to be send to telegram."""
    file_name: str
    content_type: str
    file: typing.BinaryIO


class EnumAutoName(Enum):
    """Class for enums."""
    def _generate_next_value_(name, start, count, last_values):
        return name
