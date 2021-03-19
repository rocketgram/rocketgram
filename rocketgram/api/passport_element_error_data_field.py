# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass, field

from .encrypted_passport_element_type import EncryptedPassportElementType
from .passport_element_error import PassportElementError


@dataclass(frozen=True)
class PassportElementErrorDataField(PassportElementError):
    """\
    Represents PassportElementErrorDataField object:
    https://core.telegram.org/bots/api#passportelementerrordatafield
    """

    source: str = field(init=False, default='data')

    type: EncryptedPassportElementType
    field_name: str
    data_hash: str
    message: str
