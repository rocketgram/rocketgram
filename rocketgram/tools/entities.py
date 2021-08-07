# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


import sys
from collections import namedtuple
from typing import Optional, List, Generator, Dict, Callable

from . import escape
from ..api import MessageEntity, EntityType

Tag = namedtuple('Tag', 'open close')

ENCODE_UTF16 = not sys.maxunicode == 0xffff

HTML = {
    EntityType.bold: Tag('<b>', '</b>'),
    EntityType.italic: Tag('<i>', '</i>'),
    EntityType.underline: Tag('<u>', '</u>'),
    EntityType.strikethrough: Tag('<s>', '</s>'),
    EntityType.code: Tag('<code>', '</code>'),
    EntityType.pre: Tag('<pre>', '</pre>'),
    EntityType.text_link: Tag('<a href="%s">', '</a>'),
    EntityType.text_mention: Tag('<a href="tg://user?id=%s">', '</a>'),
}

MARKDOWN = {
    EntityType.bold: Tag('*', '*'),
    EntityType.italic: Tag('_', '_'),
    EntityType.code: Tag('`', '`'),
    EntityType.pre: Tag('```\n', '```'),
    EntityType.text_link: Tag('[', '](%s)'),
    EntityType.text_mention: Tag('[', '](tg://user?id=%s)'),
}

MARKDOWN2 = MARKDOWN.copy()
MARKDOWN2.update({
    EntityType.underline: Tag('\r__\r', '\r__\r'),
    EntityType.strikethrough: Tag('~', '~'),
})


def parse(text: str, entities: List[MessageEntity], get_tag: Callable[[bool, MessageEntity], Optional[str]],
          esc: Callable[[str], str]) -> str:
    encoded = text.encode('utf-16-le') if ENCODE_UTF16 else text

    def e(start: int, end: int) -> str:
        return encoded[start * 2:end * 2].decode('utf-16-le') if ENCODE_UTF16 else encoded[start:end]

    def p(sub: List[MessageEntity], start: int, end: int) -> Generator[str, None, None]:
        for index, entity in enumerate(sub):
            if entity.offset < start:
                continue
            if entity.offset > start:
                yield esc(e(start, entity.offset))

            open_tag = get_tag(True, entity)
            if open_tag:
                yield open_tag

            start = entity.offset + entity.length
            nested = list(filter(lambda i: start > i.offset, sub[index + 1:]))

            yield from p(nested, entity.offset, start)

            close_tag = get_tag(False, entity)
            if close_tag:
                yield close_tag

        if start < end:
            yield esc(e(start, end))

    se = sorted(entities, key=lambda item: item.offset)

    return str().join(p(se, 0, len(encoded)))


def get_html_tag(is_open: bool, entity: MessageEntity) -> Optional[str]:
    tag = HTML.get(entity.type)
    if not tag:
        return None

    if entity.type == EntityType.text_link and is_open:
        return tag.open % entity.url

    if entity.type == EntityType.text_mention and is_open:
        return tag.open % entity.user.id

    return tag.open if is_open else tag.close


def get_md_tag(is_open: bool, entity: MessageEntity, tags: Dict[EntityType, Tag]) -> Optional[str]:
    tag = tags.get(entity.type)
    if not tag:
        return None

    if entity.type == EntityType.text_link and not is_open:
        return tag.close % entity.url

    if entity.type == EntityType.text_mention and not is_open:
        return tag.close % entity.user.id

    return tag.open if is_open else tag.close


def get_markdown_tag(is_open: bool, entity: MessageEntity) -> Optional[str]:
    return get_md_tag(is_open, entity, MARKDOWN)


def get_markdown2_tag(is_open: bool, entity: MessageEntity) -> Optional[str]:
    return get_md_tag(is_open, entity, MARKDOWN2)


def to_html(text: Optional[str], entities: List[MessageEntity], escape_html: bool = True) -> Optional[str]:
    if text is None:
        return None

    if entities is None:
        return text

    return parse(text, entities, get_html_tag, escape.html if escape_html else lambda t: t)


def to_markdown(text: Optional[str], entities: List[MessageEntity], escape_markdown: bool = True) -> Optional[str]:
    if text is None:
        return None

    if entities is None:
        return text

    return parse(text, entities, get_markdown_tag, escape.markdown if escape_markdown else lambda t: t)


def to_markdown2(text: Optional[str], entities: List[MessageEntity], escape_markdown2: bool = True) -> Optional[str]:
    if text is None:
        return None

    if entities is None:
        return text

    return parse(text, entities, get_markdown2_tag, escape.markdown2 if escape_markdown2 else lambda t: t)
