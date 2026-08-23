# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional

from .input_file import InputFile


@dataclass(frozen=True)
class InputStoryContentPhoto:
    """    Represents InputStoryContentPhoto object:
    https://core.telegram.org/bots/api#inputstorycontentphoto
    """

    photo: Union[InputFile, str]
    type: str = "photo"


@dataclass(frozen=True)
class InputStoryContentVideo:
    """    Represents InputStoryContentVideo object:
    https://core.telegram.org/bots/api#inputstorycontentvideo
    """

    video: Union[InputFile, str]
    type: str = "video"
    duration: Optional[float] = None
    cover_frame_timestamp: Optional[float] = None
    is_animation: Optional[bool] = None
