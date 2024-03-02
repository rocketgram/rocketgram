# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class LinkPreviewOptions:
    """\
    Represents LinkPreviewOptions object:
    https://core.telegram.org/bots/api#linkpreviewoptions
    """

    is_disabled: Optional[bool] = None
    url: Optional[str] = None
    prefer_small_media: Optional[bool] = None
    prefer_large_media: Optional[bool] = None
    show_above_text: Optional[bool] = None

    @classmethod
    def parse(cls, data: dict) -> Optional['LinkPreviewOptions']:
        if data is None:
            return None

        return cls(
            data.get('is_disabled'),
            data.get('url'),
            data.get('prefer_small_media'),
            data.get('prefer_large_media'),
            data.get('show_above_text')
        )
