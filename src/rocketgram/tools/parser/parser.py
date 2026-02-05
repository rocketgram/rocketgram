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

    @staticmethod
    def _e(text: str) -> bytes:
        return text.encode("utf-16-le")

    @staticmethod
    def _d(text: bytes) -> str:
        return text.decode("utf-16-le")

    @classmethod
    def _parse(cls, text: bytes, sub: List[MessageEntity], start: int, end: int) -> List['Element']:
        inners = []

        for index, entity in enumerate(sub):
            if entity.offset * 2 < start:
                continue
            if entity.offset * 2 > start:
                inners.append(cls._d(text[start:entity.offset * 2]))

            entity_start = entity.offset * 2
            start = entity.offset * 2 + entity.length * 2
            nested = list(filter(lambda i: i.offset * 2 < start, sub[index + 1:]))
            inners.append(cls(entity, *cls._parse(text, nested, entity_start, start)))

        if start < end:
            inners.append(cls._d(text[start:end]))

        return inners

    @classmethod
    def parse(cls, text: str, entities: Optional[List[MessageEntity]]) -> 'Element':
        if not entities:
            return cls(None, text)
        text_bytes = cls._e(text)
        return cls(None, *cls._parse(text_bytes, entities, 0, len(text_bytes)))


class Parser(Element):
    pass
