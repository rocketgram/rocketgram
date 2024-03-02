# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass, field

from .encrypted_passport_element_type import EncryptedPassportElementType
from .passport_element_error import PassportElementError


@dataclass(frozen=True)
class PassportElementErrorReverseSide(PassportElementError):
    """\
    Represents PassportElementErrorReverseSide object:
    https://core.telegram.org/bots/api#passportelementerrorreverseside
    """

    source: str = field(init=False, default='reverse_side')

    type: EncryptedPassportElementType
    file_hash: str
    message: str
