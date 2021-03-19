# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass, field
from typing import List

from .encrypted_passport_element_type import EncryptedPassportElementType
from .passport_element_error import PassportElementError


@dataclass(frozen=True)
class PassportElementErrorTranslationFiles(PassportElementError):
    """\
    Represents PassportElementErrorTranslationFiles object:
    https://core.telegram.org/bots/api#passportelementerrortranslationfiles
    """

    source: str = field(init=False, default='translation_files')

    type: EncryptedPassportElementType
    file_hashes: List[str]
    message: str
