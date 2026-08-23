# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional

from .input_file import InputFile


@dataclass(frozen=True)
class InputProfilePhotoStatic:
    """    Represents InputProfilePhotoStatic object:
    https://core.telegram.org/bots/api#inputprofilephotostatic
    """

    photo: Union[InputFile, str]
    type: str = "static"


@dataclass(frozen=True)
class InputProfilePhotoAnimated:
    """    Represents InputProfilePhotoAnimated object:
    https://core.telegram.org/bots/api#inputprofilephotoanimated
    """

    animation: Union[InputFile, str]
    type: str = "animated"
    main_frame_timestamp: Optional[float] = None
