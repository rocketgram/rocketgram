# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class ChatPermissions:
    """\
    Represents ChatPermissions object:
    https://core.telegram.org/bots/api#chatpermissions
    """

    can_send_messages: Optional[bool]
    can_send_audios: Optional[bool]
    can_send_documents: Optional[bool]
    can_send_photos: Optional[bool]
    can_send_videos: Optional[bool]
    can_send_video_notes: Optional[bool]
    can_send_voice_notes: Optional[bool]
    can_send_polls: Optional[bool]
    can_send_other_messages: Optional[bool]
    can_add_web_page_previews: Optional[bool]
    can_change_info: Optional[bool]
    can_invite_users: Optional[bool]
    can_pin_messages: Optional[bool]
    can_manage_topics: Optional[bool]

    @classmethod
    def parse(cls, data: dict) -> Optional['ChatPermissions']:
        if data is None:
            return None

        return cls(
            data.get('can_send_messages'),
            data.get('can_send_audios'),
            data.get('can_send_documents'),
            data.get('can_send_photos'),
            data.get('can_send_videos'),
            data.get('can_send_video_notes'),
            data.get('can_send_voice_notes'),
            data.get('can_send_polls'),
            data.get('can_send_other_messages'),
            data.get('can_add_web_page_previews'),
            data.get('can_change_info'),
            data.get('can_invite_users'),
            data.get('can_pin_messages'),
            data.get('can_manage_topics')
        )
