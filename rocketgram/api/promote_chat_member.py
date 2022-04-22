# Copyright (C) 2015-2022 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


import warnings
from dataclasses import dataclass
from typing import Union, Optional

from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class PromoteChatMember(BoolResultMixin, Request):
    """\
    Represents PromoteChatMember request object:
    https://core.telegram.org/bots/api#promotechatmember
    """

    chat_id: Union[int, str]
    user_id: int
    is_anonymous: Optional[bool] = None
    can_manage_chat: Optional[bool] = None
    can_change_info: Optional[bool] = None
    can_post_messages: Optional[bool] = None
    can_edit_messages: Optional[bool] = None
    can_delete_messages: Optional[bool] = None
    can_manage_video_chats: Optional[bool] = None
    can_invite_users: Optional[bool] = None
    can_restrict_members: Optional[bool] = None
    can_promote_members: Optional[bool] = None
    can_pin_messages: Optional[bool] = None

    @property
    def can_manage_voice_chats(self) -> Optional[bool]:
        warnings.warn("This field is deprecated. Use `can_manage_video_chats` instead.", DeprecationWarning)

        return self.can_manage_video_chats
