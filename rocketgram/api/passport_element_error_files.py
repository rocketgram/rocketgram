# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass, field
from typing import List

from .encrypted_passport_element_type import EncryptedPassportElementType
from .passport_element_error import PassportElementError


@dataclass(frozen=True)
class PassportElementErrorFiles(PassportElementError):
    """\
    Represents PassportElementErrorFiles object:
    https://core.telegram.org/bots/api#passportelementerrorfiles
    """

    source: str = field(init=False, default='files')

    type: EncryptedPassportElementType
    file_hashes: List[str]
    message: str
