# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from typing import Optional, List, Union, Type

from .style import Style
from ...api import MessageEntity


class Element:
    def __init__(self, message_entity: Optional[MessageEntity], *inner: Union['Element', str]):
        self._message_entity = message_entity
        self._inner = inner

    def render(self, style: Type[Style]) -> str:
        parts = (i.render(style) if isinstance(i, Element) else style.escape(i) for i in self._inner)
        return style.apply(self._message_entity, str().join(parts))

    def __repr__(self):
        return f"Tag({self._message_entity.type if self._message_entity else None}, {self._inner})"

    @classmethod
    def _parse(cls, text: str, sub: List[MessageEntity], start: int, end: int) -> List['Element']:
        inners = []

        for index, entity in enumerate(sub):
            if entity.offset < start:
                continue
            if entity.offset > start:
                inners.append(text[start:entity.offset])

            start = entity.offset + entity.length
            nested = list(filter(lambda i: start > i.offset, sub[index + 1:]))
            inners.append(cls(entity, *cls._parse(text, nested, entity.offset, start)))

        if start < end:
            inners.append(text[start:end])

        return inners

    @classmethod
    def parse(cls, text: str, entities: Optional[List[MessageEntity]]) -> 'Element':
        if not entities:
            return cls(None, text)
        return cls(None, *cls._parse(text, entities, 0, len(text)))


class Parser(Element):
    pass
