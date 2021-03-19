# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Dict, Optional, List

from . import user


@dataclass(frozen=True)
class VoiceChatParticipantsInvited:
    """\
    Represents VoiceChatParticipantsInvited object:
    https://core.telegram.org/bots/api#voicechatparticipantsinvited
    """

    users: List['user.User']

    @classmethod
    def parse(cls, data: Optional[Dict]) -> Optional['VoiceChatParticipantsInvited']:
        if data is None:
            return None

        return cls([user.User.parse(u) for u in data['users']])
