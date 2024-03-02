# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class WriteAccessAllowed:
    """\
    Represents WriteAccessAllowed object:
    https://core.telegram.org/bots/api#writeaccessallowed
    """

    from_request: Optional[bool] = None
    web_app_name: Optional[str] = None
    from_attachment_menu: Optional[bool] = None

    @classmethod
    def parse(cls, data: dict) -> Optional['WriteAccessAllowed']:
        if data is None:
            return None

        return cls(
            data.get('from_request'),
            data.get('web_app_name'),
            data.get('from_attachment_menu')
        )
