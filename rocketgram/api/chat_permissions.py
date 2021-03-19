# Copyright (C) 2015-2021 by Vd.
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
    can_send_media_messages: Optional[bool]
    can_send_polls: Optional[bool]
    can_send_other_messages: Optional[bool]
    can_add_web_page_previews: Optional[bool]
    can_change_info: Optional[bool]
    can_invite_users: Optional[bool]
    can_pin_messages: Optional[bool]

    @classmethod
    def parse(cls, data: dict) -> Optional['ChatPermissions']:
        if data is None:
            return None

        return cls(data.get('can_send_messages'), data.get('can_send_media_messages'), data.get('can_send_polls'),
                   data.get('can_send_other_messages'), data.get('can_add_web_page_previews'),
                   data.get('can_change_info'), data.get('can_invite_users'), data.get('can_pin_messages'))
