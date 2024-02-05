# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from enum import auto

from .utils import EnumAutoName


class ChatActionType(EnumAutoName):
    """\
    Chat action type:
    https://core.telegram.org/bots/api#sendchataction
    """

    typing = auto()
    upload_photo = auto()
    record_video = auto()
    upload_video = auto()
    record_audio = auto()
    upload_audio = auto()
    record_voice = auto()
    upload_voice = auto()
    upload_document = auto()
    choose_sticker = auto()
    find_location = auto()
    record_video_note = auto()
    upload_video_note = auto()
