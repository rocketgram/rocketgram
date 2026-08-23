# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, List, Optional, Union

from .inaccessible_message import InaccessibleMessage
from .message_entity import MessageEntity

if TYPE_CHECKING:
    from .message import Message


@dataclass(frozen=True)
class PollOptionDeleted:
    """\
    Represents PollOptionDeleted object:
    https://core.telegram.org/bots/api#polloptiondeleted
    """

    poll_message: Optional[Union[Message, InaccessibleMessage]]
    option_persistent_id: str
    option_text: str
    option_text_entities: Optional[List[MessageEntity]]

    @classmethod
    def parse(cls, data: dict) -> Optional['PollOptionDeleted']:
        if data is None:
            return None

        from .message import Message

        poll_message_data = data.get('poll_message')
        poll_message = None
        if poll_message_data is not None:
            poll_message = InaccessibleMessage.parse(poll_message_data) \
                if poll_message_data.get('date') == 0 else Message.parse(poll_message_data)
        return cls(
            poll_message,
            data['option_persistent_id'],
            data['option_text'],
            [MessageEntity.parse(d) for d in data['option_text_entities']]
            if 'option_text_entities' in data else None,
        )
