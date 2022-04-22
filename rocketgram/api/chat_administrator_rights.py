# Copyright (C) 2015-2022 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class ChatAdministratorRights:
    """\
    Represents ChatAdministratorRights object:
    https://core.telegram.org/bots/api#chatadministratorrights
    """

    is_anonymous: bool
    can_manage_chat: bool
    can_delete_messages: bool
    can_manage_video_chats: bool
    can_restrict_members: bool
    can_promote_members: bool
    can_change_info: bool
    can_invite_users: bool
    can_post_messages: bool
    can_edit_messages: bool
    can_pin_messages: bool

    @classmethod
    def parse(cls, data: dict) -> Optional['ChatAdministratorRights']:
        if data is None:
            return None

        return cls(data['is_anonymous'], data['can_manage_chat'], data['can_delete_messages'],
                   data['can_manage_video_chats'], data['can_restrict_members'], data['can_promote_members'],
                   data['can_change_info'], data['can_invite_users'], data['can_post_messages'],
                   data['can_edit_messages'], data['can_pin_messages'])
