# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from . import chat
from .unique_gift_backdrop import UniqueGiftBackdrop
from .unique_gift_colors import UniqueGiftColors
from .unique_gift_model import UniqueGiftModel
from .unique_gift_symbol import UniqueGiftSymbol


@dataclass(frozen=True)
class UniqueGift:
    """\
    Represents UniqueGift object:
    https://core.telegram.org/bots/api#uniquegift
    """

    gift_id: str
    base_name: str
    name: str
    number: int
    model: UniqueGiftModel
    symbol: UniqueGiftSymbol
    backdrop: UniqueGiftBackdrop
    is_premium: Optional[bool]
    is_burned: Optional[bool]
    is_from_blockchain: Optional[bool]
    colors: Optional[UniqueGiftColors]
    publisher_chat: Optional['chat.Chat']

    @classmethod
    def parse(cls, data: dict) -> Optional['UniqueGift']:
        if data is None:
            return None

        return cls(
            data['gift_id'],
            data['base_name'],
            data['name'],
            data['number'],
            UniqueGiftModel.parse(data['model']),
            UniqueGiftSymbol.parse(data['symbol']),
            UniqueGiftBackdrop.parse(data['backdrop']),
            data.get('is_premium'),
            data.get('is_burned'),
            data.get('is_from_blockchain'),
            UniqueGiftColors.parse(data.get('colors')),
            chat.Chat.parse(data.get('publisher_chat')),
        )
