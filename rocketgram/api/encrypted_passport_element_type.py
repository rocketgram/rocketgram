# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from enum import auto

from .utils import EnumAutoName


class EncryptedPassportElementType(EnumAutoName):
    personal_details = auto()
    passport = auto()
    driver_license = auto()
    identity_card = auto()
    internal_passport = auto()
    address = auto()
    utility_bill = auto()
    bank_statement = auto()
    rental_agreement = auto()
    passport_registration = auto()
    temporary_registration = auto()
    phone_number = auto()
    email = auto()
