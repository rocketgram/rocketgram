# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List

from .encrypted_credentials import EncryptedCredentials
from .encrypted_passport_element import EncryptedPassportElement


@dataclass(frozen=True)
class PassportData:
    """\
    Represents PassportData object:
    https://core.telegram.org/bots/api#passportdata
    """

    data: List[EncryptedPassportElement]
    credentials: EncryptedCredentials

    @classmethod
    def parse(cls, data: dict) -> Optional['PassportData']:
        if data is None:
            return None

        list_data = [EncryptedPassportElement.parse(s) for s in data['data']]
        credentials = EncryptedCredentials.parse(data['credentials'])

        return cls(list_data, credentials)
