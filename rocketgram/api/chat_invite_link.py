# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from datetime import datetime
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
    is_primary: bool
    is_revoked: bool
    expire_date: Optional[datetime]
    member_limit: Optional[int]

    @classmethod
    def parse(cls, data: Optional[Dict]) -> Optional['ChatInviteLink']:
        if data is None:
            return None

        expire_date = datetime.utcfromtimestamp(data['expire_date']) if 'expire_date' in data else None

        return cls(data['invite_link'], user.User.parse(data['creator']), data['is_primary'], data['is_revoked'],
                   expire_date, data['member_limit'])
