# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional

from .input_file import InputFile


@dataclass(frozen=True)
class InputPaidMediaPhoto:
    """    Represents InputPaidMediaPhoto object:
    https://core.telegram.org/bots/api#inputpaidmediaphoto
    """

    type: str = "photo"
    media: Union[InputFile, str] = ""


@dataclass(frozen=True)
class InputPaidMediaVideo:
    """    Represents InputPaidMediaVideo object:
    https://core.telegram.org/bots/api#inputpaidmediavideo
    """

    media: Union[InputFile, str] = ""
    type: str = "video"
    thumbnail: Optional[Union[InputFile, str]] = None
    width: Optional[int] = None
    height: Optional[int] = None
    duration: Optional[int] = None
    supports_streaming: Optional[bool] = None


@dataclass(frozen=True)
class InputPaidMediaLivePhoto:
    """    Represents InputPaidMediaLivePhoto object:
    https://core.telegram.org/bots/api#inputpaidmedialivephoto
    """

    media: Union[InputFile, str]
    photo: Union[InputFile, str]
    type: str = "live_photo"
