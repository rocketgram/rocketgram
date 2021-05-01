# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from enum import auto

from .utils import EnumAutoName


class MessageType(EnumAutoName):
    text = auto()
    audio = auto()
    document = auto()
    animation = auto()
    game = auto()
    photo = auto()
    sticker = auto()
    video = auto()
    voice = auto()
    video_note = auto()
    contact = auto()
    location = auto()
    venue = auto()
    poll = auto()
    dice = auto()
    new_chat_members = auto()
    left_chat_member = auto()
    new_chat_title = auto()
    new_chat_photo = auto()
    delete_chat_photo = auto()
    group_chat_created = auto()
    supergroup_chat_created = auto()
    channel_chat_created = auto()
    migrate_to_chat_id = auto()
    migrate_from_chat_id = auto()
    pinned_message = auto()
    invoice = auto()
    successful_payment = auto()
    connected_website = auto()
    passport_data = auto()
    proximity_alert_triggered = auto()
    voice_chat_scheduled = auto()
    voice_chat_started = auto()
    voice_chat_ended = auto()
    voice_chat_participants_invited = auto()
    message_auto_delete_timer_changed = auto()
    unknown = auto()
