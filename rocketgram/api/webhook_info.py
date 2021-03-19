# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Optional

from .update_type import UpdateType


@dataclass(frozen=True)
class WebhookInfo:
    """\
    Represents WebhookInfo object:
    https://core.telegram.org/bots/api#getwebhookinfo
    """

    url: str
    has_custom_certificate: bool
    pending_update_count: int
    ip_address: Optional[str]
    last_error_date: Optional[datetime]
    last_error_message: Optional[str]
    max_connections: Optional[int]
    allowed_updates: Optional[List[UpdateType]]

    @classmethod
    def parse(cls, data: Optional[Dict]) -> Optional['WebhookInfo']:
        if data is None:
            return None

        last_error_date = datetime.utcfromtimestamp(data['last_error_date']) if 'last_error_date' in data else None
        allowed_updates = [UpdateType(m) for m in data['allowed_updates']] if 'allowed_updates' in data else None

        return cls(data['url'], data['has_custom_certificate'], data['pending_update_count'], data.get('ip_address'),
                   last_error_date, data.get('last_error_message'), data.get('max_connections'), allowed_updates)
