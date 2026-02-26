# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class BusinessBotRights:
    """\
    Represents BusinessBotRights object:
    https://core.telegram.org/bots/api#businessbotrights
    """

    can_reply: Optional[bool]
    can_read_messages: Optional[bool]
    can_delete_sent_messages: Optional[bool]
    can_delete_all_messages: Optional[bool]
    can_edit_name: Optional[bool]
    can_edit_bio: Optional[bool]
    can_edit_profile_photo: Optional[bool]
    can_edit_username: Optional[bool]
    can_change_gift_settings: Optional[bool]
    can_view_gifts_and_stars: Optional[bool]
    can_convert_gifts_to_stars: Optional[bool]
    can_transfer_and_upgrade_gifts: Optional[bool]
    can_transfer_stars: Optional[bool]
    can_manage_stories: Optional[bool]

    @classmethod
    def parse(cls, data: dict) -> Optional['BusinessBotRights']:
        if data is None:
            return None

        return cls(
            data.get('can_reply'),
            data.get('can_read_messages'),
            data.get('can_delete_sent_messages'),
            data.get('can_delete_all_messages'),
            data.get('can_edit_name'),
            data.get('can_edit_bio'),
            data.get('can_edit_profile_photo'),
            data.get('can_edit_username'),
            data.get('can_change_gift_settings'),
            data.get('can_view_gifts_and_stars'),
            data.get('can_convert_gifts_to_stars'),
            data.get('can_transfer_and_upgrade_gifts'),
            data.get('can_transfer_stars'),
            data.get('can_manage_stories'),
        )
