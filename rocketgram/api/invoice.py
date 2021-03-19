# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Invoice:
    """\
    Represents Invoice object:
    https://core.telegram.org/bots/api#invoice
    """

    title: str
    description: str
    start_parameter: str
    currency: str
    total_amount: str

    @classmethod
    def parse(cls, data: dict) -> Optional['Invoice']:
        if data is None:
            return None

        return cls(data['title'], data['description'], data['start_parameter'], data['currency'], data['total_amount'])
