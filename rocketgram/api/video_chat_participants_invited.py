# Copyright (C) 2015-2022 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Dict, Optional, Tuple

from . import user


@dataclass(frozen=True)
class VideoChatParticipantsInvited:
    """\
    Represents VideoChatParticipantsInvited object:
    https://core.telegram.org/bots/api#voicechatparticipantsinvited
    """

    users: Tuple['user.User', ...]

    @classmethod
    def parse(cls, data: Optional[Dict]) -> Optional['VideoChatParticipantsInvited']:
        if data is None:
            return None

        return cls(tuple(user.User.parse(u) for u in data['users']))
