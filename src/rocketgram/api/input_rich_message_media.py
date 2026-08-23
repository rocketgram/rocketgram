# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union

from .input_media_animation import InputMediaAnimation
from .input_media_audio import InputMediaAudio
from .input_media_photo import InputMediaPhoto
from .input_media_video import InputMediaVideo
from .input_media_voice_note import InputMediaVoiceNote


@dataclass(frozen=True)
class InputRichMessageMedia:
    """\
    Represents InputRichMessageMedia object:
    https://core.telegram.org/bots/api#inputrichmessagemedia
    """

    id: str
    media: Union[
        InputMediaAnimation,
        InputMediaAudio,
        InputMediaPhoto,
        InputMediaVideo,
        InputMediaVoiceNote,
    ]
