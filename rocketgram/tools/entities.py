# Copyright (C) 2015-2019 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


import sys
from dataclasses import dataclass
from typing import Optional, List

from . import escape
from ..update import User, MessageEntity, EntityType


@dataclass(frozen=True)
class EntityItem:
    entity_type: Optional[EntityType]
    text: str
    url: Optional[str]
    user: Optional[User]


def parse(text: str, entities: List[MessageEntity]) -> List[EntityItem]:
    if not entities:
        return [EntityItem(None, text, None, None)]

    if sys.maxunicode == 0xffff:
        encoded = False
    else:
        encoded = True
        text = text.encode('utf-16-le')

    parsed = list()
    idx = 0
    for e in entities:
        offset = e.offset * 2 if encoded else e.offset
        length = e.length * 2 if encoded else e.length

        if idx < offset:
            t = text[idx:offset]
            if encoded:
                t = t.decode('utf-16-le')
            parsed.append(EntityItem(None, t, None, None))

        t = text[offset:offset + length]
        if encoded:
            t = t.decode('utf-16-le')
        parsed.append(EntityItem(e.entity_type, t, e.url, e.user))

        idx = offset + length

    if idx < len(text):
        t = text[idx:len(text)]
        if encoded:
            t = t.decode('utf-16-le')
        parsed.append(EntityItem(None, t, None, None))
    return parsed


def to_html(text: Optional[str], entities: List[MessageEntity], escape_html: bool = True) -> Optional[str]:
    if text is None:
        return None

    esc = escape.html if escape_html else lambda tx: tx

    result = str()
    for m in parse(text, entities):
        t = esc(m.text)
        if m.entity_type is EntityType.bold:
            result += f'<b>{t}</b>'
        elif m.entity_type is EntityType.italic:
            result += f'<i>{t}</i>'
        elif m.entity_type is EntityType.code:
            result += f'<code>{t}</code>'
        elif m.entity_type is EntityType.pre:
            result += f'<pre>{t}</pre>'
        elif m.entity_type is EntityType.text_link:
            result += f'<a href="{m.url}">{t}</a>'
        elif m.entity_type is EntityType.text_mention:
            result += f'<a href="tg://user?id={m.user.user_id}">{t}</a>'
        else:
            result += t

    return result


def to_markdown(text: Optional[str], entities: List[MessageEntity], escape_markdown: bool = True) -> Optional[str]:
    if text is None:
        return None

    esc = escape.markdown if escape_markdown else lambda tx: tx

    result = str()
    for m in parse(text, entities):
        t = esc(m.text)
        if m.entity_type is EntityType.bold:
            result += f'*{t}*'
        elif m.entity_type is EntityType.italic:
            result += f'_{t}_'
        elif m.entity_type is EntityType.code:
            result += f'`{t}`'
        elif m.entity_type is EntityType.pre:
            result += f'```\n{t}```'
        elif m.entity_type is EntityType.text_link:
            result += f'[{t}]({m.url})'
        elif m.entity_type is EntityType.text_mention:
            result += f'[{t}](tg://user?id={m.user.user_id})'
        else:
            result += t

    return result
