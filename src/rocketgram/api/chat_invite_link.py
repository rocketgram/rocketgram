# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Dict, Optional

from . import user


@dataclass(frozen=True)
class ChatInviteLink:
    """\
    Represents ChatInviteLink object:
    https://core.telegram.org/bots/api#chatinvitelink
    """

    invite_link: str
    creator: 'user.User'
    creates_join_request: bool
    is_primary: bool
    is_revoked: bool
    name: Optional[str]
    expire_date: Optional[datetime]
    member_limit: Optional[int]
    pending_join_request_count: Optional[int]

    @classmethod
    def parse(cls, data: Optional[Dict]) -> Optional['ChatInviteLink']:
        if data is None:
            return None

        expire_date = datetime.fromtimestamp(data['expire_date'], tz=timezone.utc) if 'expire_date' in data else None

        return cls(data['invite_link'], user.User.parse(data['creator']), data['creates_join_request'],
                   data['is_primary'], data['is_revoked'], data.get('name'), expire_date, data.get('member_limit'),
                   data.get('pending_join_request_count'))
