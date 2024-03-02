# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List

from .encrypted_passport_element_type import EncryptedPassportElementType
from .password_file import PassportFile


@dataclass(frozen=True)
class EncryptedPassportElement:
    """\
    Represents EncryptedPassportElement object:
    https://core.telegram.org/bots/api#encryptedpassportelement

    Differences in field names:
    type -> encrypted_passport_element_type
    """

    type: EncryptedPassportElementType
    data: Optional[str]
    phone_number: Optional[str]
    email: Optional[str]
    files: Optional[List[PassportFile]]
    front_side: Optional[PassportFile]
    reverse_side: Optional[PassportFile]
    selfie: Optional[PassportFile]
    translation: Optional[List[PassportFile]]
    hash: str

    @classmethod
    def parse(cls, data: dict) -> Optional['EncryptedPassportElement']:
        if data is None:
            return None

        files = [PassportFile.parse(s) for s in data['files']] if 'files' in data else None
        translation = [PassportFile.parse(s) for s in data['translation']] if 'translation' in data else None

        return cls(EncryptedPassportElementType(data['type']), data.get('data'), data.get('phone_number'),
                   data.get('email'), files, PassportFile.parse(data.get('front_side')),
                   PassportFile.parse(data.get('reverse_side')), PassportFile.parse(data.get('selfie')), translation,
                   data['hash'])
