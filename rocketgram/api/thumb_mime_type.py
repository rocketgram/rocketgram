# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from enum import Enum


class ThumbMimeType(Enum):
    """\
    Mime type for gif and mpeg4gif inline results

    https://core.telegram.org/bots/api#inlinequeryresultgif
    https://core.telegram.org/bots/api#inlinequeryresultmpeg4gif
    """

    image_jpeg = "image/jpeg"
    image_gif = "image/gif"
    video_mp4 = "video/mp4"
