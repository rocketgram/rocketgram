# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from typing import Union

from .input_media_animation import InputMediaAnimation
from .input_media_link import InputMediaLink
from .input_media_live_photo import InputMediaLivePhoto
from .input_media_location import InputMediaLocation
from .input_media_photo import InputMediaPhoto
from .input_media_sticker import InputMediaSticker
from .input_media_venue import InputMediaVenue
from .input_media_video import InputMediaVideo


InputPollOptionMedia = Union[
    InputMediaAnimation,
    InputMediaLink,
    InputMediaLivePhoto,
    InputMediaLocation,
    InputMediaPhoto,
    InputMediaSticker,
    InputMediaVenue,
    InputMediaVideo,
]
