# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Dict, Optional


@dataclass(frozen=True)
class VoiceChatStarted:
    """\
    Represents VoiceChatStarted object:
    https://core.telegram.org/bots/api#voicechatstarted
    """

    @classmethod
    def parse(cls, data: Optional[Dict]) -> Optional['VoiceChatStarted']:
        if data is None:
            return None

        return cls()
