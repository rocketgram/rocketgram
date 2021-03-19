# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class EncryptedCredentials:
    """\
    Represents EncryptedCredentials object:
    https://core.telegram.org/bots/api#encryptedcredentials
    """

    data: str
    hash: str
    secret: str

    @classmethod
    def parse(cls, data: dict) -> Optional['EncryptedCredentials']:
        if data is None:
            return None

        return cls(data['data'], data['hash'], data['secret'])
