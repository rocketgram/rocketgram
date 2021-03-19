# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .user import User


@dataclass(frozen=True)
class ProximityAlertTriggered:
    """\
    Represents ProximityAlertTriggered object:
    https://core.telegram.org/bots/api#proximityalerttriggered
    """

    traveler: User
    watcher: User
    distance: int

    @classmethod
    def parse(cls, data: dict) -> Optional['ProximityAlertTriggered']:
        if data is None:
            return None

        return cls(data['traveler'], data['watcher'], data['distance'])
